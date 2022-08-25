import os
import zipfile
import Classes.helper as hp
from .Addon import Addon

class GW2Radial(Addon):
    def __init__(self):
        super(GW2Radial, self).__init__()
        self.ID = 8
        self.Name = "GW2Radial"
        self.Author = "Friendly0Fire"
        self.Github = "Friendly0Fire/GW2Radial"
        self.Path = "addons\\gw2radial"
        self.UnzippedFileName = "gw2addon_gw2radial.dll"
        self.PathInZip = "gw2radial/gw2addon_gw2radial.dll"
        self.Description = """An ArenaNET-approvedTM addon to show a convenient, customizable radial menu overlay to select a mount, novelty item and more, on the fly, for Guild Wars 2."""

    def download_file(self, ssm, enable_progress_bar):
        url = "https://github.com/% s/releases/latest/download/% s" % (self.Github, self.FileName)
        folder_path = os.path.join(ssm.root_path, self.Path)
        zip_path = os.path.join(folder_path, self.FileName)
        hp.download_file(url, zip_path, enable_progress_bar)

        # unzip the file, but the file is in a folder within
        file_path = os.path.join(folder_path, self.UnzippedFileName)
        try:
            with zipfile.ZipFile(zip_path) as z:
                with open(file_path, 'wb') as f:
                    f.write(z.read(self.PathInZip))
        except:
            print("Invalid file")
            return False

        # delete zip file
        os.remove(zip_path)
        return True

    def delete_file(self, ssm):
        # Overridden because in this case we delete the unzipped file, not the originally downloaded archive
        full_path = os.path.join(ssm.root_path, self.Path, self.UnzippedFileName)
        if os.path.exists(full_path):
            os.remove(full_path)
        return True