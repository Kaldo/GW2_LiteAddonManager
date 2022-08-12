import os
import zipfile
import helper as hp
from .Addon import Addon

class BlishHudArcdps(Addon):
    def __init__(self):
        super(BlishHudArcdps, self).__init__()
        self.ID = 5
        self.Name = "BlishHUD ArcDPS"
        self.Author = "blish-hud"
        self.Github = "blish-hud/arcdps-bhud"
        self.Path = "addons\\arcdps"
        self.UnzippedFileName = "arcdps_bhud.dll"
        self.Description = """This is a plugin that uses the Arcdps Combat API and exposes some of the data to Blish HUD."""

    def download_file(self, ssm, enable_progress_bar):
        url = "https://github.com/% s/releases/latest/download/% s" % (self.Github, self.FileName)
        folder_path = os.path.join(ssm.root_path, self.Path)
        zip_file_path = os.path.join(folder_path, self.FileName)
        if self.SaveFileAs is not None:
            zip_file_path = os.path.join(folder_path, self.SaveFileAs)
        hp.download_file(url, zip_file_path, enable_progress_bar)

        # unzip the file
        try:
            with zipfile.ZipFile(zip_file_path) as z:
                z.extractall(os.path.join(ssm.root_path, self.Path))
        except:
            print("Invalid file")
            return False

        # delete zip file
        os.remove(zip_file_path)
        return True

    def delete_file(self, ssm):
        # Overridden because in this case we delete the unzipped file, not the originally downloaded archive
        full_path = os.path.join(ssm.root_path, self.Path, self.UnzippedFileName)
        if os.path.exists(full_path):
            os.remove(full_path)
        return True