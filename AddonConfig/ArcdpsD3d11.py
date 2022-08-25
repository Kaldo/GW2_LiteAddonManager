from .Addon import Addon
from .Addon import AddonStatus
import Classes.helper as hp
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
        self.Description = """don't be a dick.
by default, holding alt and shift is required for hotkeys, t is the hotkey for options.
left click on windows to interact.
right click on windows to bring up their independent options (if available)."""

    def download_file(self, ssm, enable_progress_bar):
        file_path = os.path.join(ssm.root_path, self.Path, self.FileName)
        hp.download_file(self.DownloadUrl, file_path, enable_progress_bar)
        return True

    def update_version_info(self):
        if self.AvailableVersion is not None:
            return True
        checksum_url = "https://www.deltaconnected.com/arcdps/x64/d3d11.dll.md5sum"
        with requests.get(checksum_url) as r:
            if r.status_code == 200:
                self.AvailableVersion = r.text.split(' ', 1)[0]
                return True
        self.AvailableVersion = None
        return False