import os
import zipfile
import helper as hp
from .Addon import Addon
from .Addon import AddonStatus

class GW2AddonLoader(Addon):
    def __init__(self):
        super(GW2AddonLoader, self).__init__()
        self.ID = 14
        self.Name = "GW2 Addon Loader"
        self.Author = "gw2-addon-loader"
        self.Github = "gw2-addon-loader/loader-core"
        self.Path = ""
        self.IsMandatory = True
        self.Description = "Core addon loading library for Guild wars 2"

    def download_file(self, ssm, enable_progress_bar):
        url = "https://github.com/% s/releases/latest/download/% s" % (self.Github, self.FileName)
        folder_path = os.path.join(ssm.root_path, self.Path)
        zip_path = os.path.join(folder_path, self.FileName)
        hp.download_file(url, zip_path, enable_progress_bar)

        # unzip the file, but the file is in a folder within
        try:
            with zipfile.ZipFile(zip_path) as z:
                with open(os.path.join(folder_path, "addonLoader.dll"), 'wb') as f:
                    f.write(z.read("addonLoader.dll"))
                with open(os.path.join(folder_path, "d3d11.dll"), 'wb') as f:
                    f.write(z.read("d3d11.dll"))
                with open(os.path.join(folder_path, "dxgi.dll"), 'wb') as f:
                    f.write(z.read("dxgi.dll"))
        except:
            print("Invalid file")
            return False

        # delete zip file
        os.remove(zip_path)
        return True

    def delete_file(self, ssm):
        # Overridden because in this case we delete the unzipped file, not the originally downloaded archive
        full_path = os.path.join(ssm.root_path, self.Path, "addonLoader.dll")
        if os.path.exists(full_path):
            os.remove(full_path)
        full_path = os.path.join(ssm.root_path, self.Path, "d3d11.dll")
        if os.path.exists(full_path):
            os.remove(full_path)
        full_path = os.path.join(ssm.root_path, self.Path, "dxgi.dll")
        if os.path.exists(full_path):
            os.remove(full_path)
        return True