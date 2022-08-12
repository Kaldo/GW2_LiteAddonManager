import os
import zipfile
import helper as hp
from .Addon import Addon
from .Addon import AddonStatus

class GW2AddonD3D9Wrapper(Addon):
    def __init__(self):
        super(GW2AddonD3D9Wrapper, self).__init__()
        self.ID = 15
        self.Name = "GW2 d3d9 Wrapper"
        self.Author = "gw2-addon-loader"
        self.Github = "gw2-addon-loader/d3d9_wrapper"
        self.Path = "addons"
        self.IsMandatory = True
        self.Description = """Wrapper for d3d9 API that includes hooking and custom d3d9 loading"""

    def download_file(self, ssm, enable_progress_bar):
        url = "https://github.com/% s/releases/latest/download/% s" % (self.Github, self.FileName)
        folder_path = os.path.join(ssm.root_path, self.Path)
        zip_path = os.path.join(folder_path, self.FileName)
        hp.download_file(url, zip_path, enable_progress_bar)

        # unzip the file
        try:
            with zipfile.ZipFile(zip_path) as z:
                z.extractall(folder_path)
        except:
            print("Invalid file")
            return False

        # delete zip file
        os.remove(zip_path)
        return True

    def delete_file(self, ssm):
        # Overridden because in this case we delete the unzipped file, not the originally downloaded archive
        full_path = os.path.join(ssm.root_path, self.Path, "gw2addon_d3d9_wrapper.dll")
        if os.path.exists(full_path):
            os.remove(full_path)
        full_path = os.path.join(ssm.root_path, self.Path, "gw2addon_d3d9_wrapper.exp")
        if os.path.exists(full_path):
            os.remove(full_path)
        full_path = os.path.join(ssm.root_path, self.Path, "gw2addon_d3d9_wrapper.lib")
        if os.path.exists(full_path):
            os.remove(full_path)
        full_path = os.path.join(ssm.root_path, self.Path, "gw2addon_d3d9_wrapper.pdb")
        if os.path.exists(full_path):
            os.remove(full_path)
        return True