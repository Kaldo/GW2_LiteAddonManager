import os
import enum
import helper as hp
import webbrowser

class AddonStatus(enum.Enum):
    NOT_INSTALLED = 1
    INSTALLED = 2
    PENDING_UPDATE = 3
    UNREACHABLE = 4

class Addon:
    """
    The default implementation assumes a github repository.
    ...
    Config parameters:
        ID : int
            internal reference for use with user settings
        Name : str
            name of the addon that will be displayed to the user
        Author : str
            name of the author/owner/maintainer of the addon
        Github : str
            identifier for the github repository, user/reponame
        Path : str
            relative path to the folder where the file should be stored
        FileName : str
            name of the file that will be downloaded and put into Path
        SaveFileAs : str
            if provided, the file will be renamed to this during the save
        IsMandatory : bool
            if True, addon will be automatically installed at first run and cannot be removed
        Description : str
            displayed in addon detailed information
    ...
    Properties:
        Index : int
            temporary identifier for user selection
        AddonStatus : enum
            displays the current installation status of the addon for the user
        InstalledVersion : str
            user setting to store the last downloaded version of the addon
        AvailableVersion : str
            filled when we do a request and look up the newest available addon version in the repo
    ...
    Methods:
        install - main wrapper for sub-methods that can be easily overridden
        pre_install
        download_file
        post_install
        uninstall - main wrapper for sub-methods that can be easily overridden
        pre_uninstall
        delete_file
        post_uninstall
        check_for_updates
        update_user_data
        check_if_file_exists
    """
    def __init__(self):
        # configuration constants
        self.ID = None
        self.Name = None
        self.Author = None
        self.Github = None
        self.Website = None
        self.DownloadUrl = None
        self.ApiUrl = None
        self.Path = None
        self.FileName = None
        self.SaveFileAs = None
        self.RequiresAddons = None
        self.IsMandatory = None
        self.Description = None
        # dynamic data
        self.Index = None
        self.AddonStatus = AddonStatus.NOT_INSTALLED
        self.InstalledVersion = None
        self.AvailableVersion = None

    def install(self, ssm, enable_progress_bar = True):
        ssm.console.print("Installing...")
        # TODO: dependency check
        # TODO: compatibility check
        if self.pre_install(ssm) == False:
            return False
        if self.download_file(ssm, enable_progress_bar) == False:
            return False
        if self.post_install(ssm) == False:
            return False
        self.update_user_data(ssm)
        return True

    def pre_install(self, ssm):
        # get newest available version
        if self.AvailableVersion == None or self.FileName == None:
            self.check_for_updates()
        if self.AvailableVersion == None:
            return False
        folder_path = os.path.join(ssm.root_path, self.Path)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        return True
    
    def download_file(self, ssm, enable_progress_bar):
        # download_url = "https://github.com/% s/releases/download" % (self.Github)
        # url = "% s/% s/% s" % (download_url, self.AvailableVersion, self.FileName)
        url = "https://github.com/% s/releases/latest/download/% s" % (self.Github, self.FileName)
        folder_path = os.path.join(ssm.root_path, self.Path)
        file_path = os.path.join(folder_path, self.FileName)
        if self.SaveFileAs is not None:
            file_path = os.path.join(folder_path, self.SaveFileAs)
        hp.download_file(url, file_path, enable_progress_bar)
        return True

    def post_install(self, ssm):
        self.AddonStatus = AddonStatus.INSTALLED
        self.InstalledVersion = self.AvailableVersion
        return True

    def uninstall(self, ssm):
        if self.pre_uninstall(ssm) == False:
            return False
        if self.delete_file(ssm) == False:
            return False
        if self.post_uninstall(ssm) == False:
            return False
        self.update_user_data(ssm)
        return True

    def pre_uninstall(self, ssm):
        if self.IsMandatory == True:
            ssm.console.print("Cannot uninstall mandatory plugins.")
            return False
        return True

    def delete_file(self, ssm):
        file_name = self.SaveFileAs if self.SaveFileAs is not None else self.FileName
        folder_path = os.path.join(ssm.root_path, self.Path)
        file_path = os.path.join(folder_path, file_name)
        if self.SaveFileAs is not None:
            file_path = os.path.join(folder_path, self.SaveFileAs)
        if os.path.exists(file_path):
            os.remove(file_path)
        return True
    
    def post_uninstall(self, ssm):
        self.AddonStatus = AddonStatus.NOT_INSTALLED
        self.InstalledVersion = None
        return True

    def check_for_updates(self):
        if self.AvailableVersion is not None:
            return True

        github_info = hp.get_github_latest_release_info(self.Github)
        if github_info == None:
            self.AvailableVersion = AddonStatus.UNREACHABLE.name
            return False
        self.FileName = github_info['file_name']
        self.AvailableVersion = github_info['version']

        if self.AvailableVersion == self.InstalledVersion:
            self.AddonStatus = AddonStatus.INSTALLED
        elif self.InstalledVersion is not None:
            self.AddonStatus = AddonStatus.PENDING_UPDATE
        return True

    def update_user_data(self, ssm):
        ssm.udm.set_version(self.ID, self.InstalledVersion)

    def check_if_file_exists(self):
        pass

    def get_website_url(self):
        if self.Github is not None:
            return "https://github.com/% s/" % (self.Github)
        elif self.Website is not None:
            return self.Website
        return None

    def open_website(self):
        website_url = self.get_website_url()
        if website_url is None:
            return False
        browser = webbrowser.get()
        browser.open_new(website_url)
        return True

    def open_info_page(self):
        pass