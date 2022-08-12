from .Addon import Addon
from .Addon import AddonStatus
import helper as hp
import os
import requests

class ArcdpsD3d11(Addon):
    def __init__(self):
        super(ArcdpsD3d11, self).__init__()
        self.ID = 1
        self.Name = "ArcDPS d3d11"
        self.Author = "deltaconnected"
        self.Website = "https://www.deltaconnected.com/arcdps/"
        self.DownloadUrl = "https://www.deltaconnected.com/arcdps/x64/d3d11.dll"
        self.Path = "addons\\arcdps"
        self.FileName = "gw2addon_arcdps.dll"
        self.ChecksumUrl = "https://www.deltaconnected.com/arcdps/x64/d3d11.dll.md5sum"

    def download_file(self, ssm, enable_progress_bar):
        file_path = os.path.join(ssm.root_path, self.Path, self.FileName)
        hp.download_file(self.DownloadUrl, file_path, enable_progress_bar)
        return True

    def check_for_updates(self):
        if self.AvailableVersion is not None:
            return True
        with requests.get(self.ChecksumUrl) as r:
            if r.status_code == 200:
                self.AvailableVersion = r.text.split(' ', 1)[0]
                return True
        self.AvailableVersion = AddonStatus.UNREACHABLE.name
        return False