import os
import zipfile
import Classes.helper as hp
from .Addon import Addon

class ArcdpsUploader(Addon):
    def __init__(self):
        super(ArcdpsUploader, self).__init__()
        self.ID = 13
        self.Name = "ArcDPS Uploader"
        self.Author = "nbarrios"
        self.Github = "nbarrios/arcdps-uploader"
        self.Path = "addons\\arcdps"
        self.UnzippedFileName = "d3d9_uploader.dll"
        self.SaveFileAs = "d3d9_uploader.dll" # d3d9_arcdps_uploader.dll ?
    
    def download_file(self, ssm):
        url = "https://github.com/% s/releases/latest/download/% s" % (self.Github, self.FileName)
        folder_path = os.path.join(ssm.root_path, self.Path)
        zip_file_path = os.path.join(folder_path, self.FileName)
        if self.SaveFileAs is not None:
            zip_file_path = os.path.join(folder_path, self.SaveFileAs)
        hp.download_file(url, zip_file_path)

        # unzip the file
        file_path = os.path.join(folder_path, self.UnzippedFileName)
        try:
            with zipfile.ZipFile(zip_file_path) as z:
                with open(file_path, 'wb') as f:
                    f.write(z.read(self.UnzippedFileName))
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