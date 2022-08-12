from .Addon import Addon

class ArcdpsUnofficialExtras(Addon):
    def __init__(self):
        super(ArcdpsUnofficialExtras, self).__init__()
        self.ID = 2
        self.Name = "ArcDPS Unofficial Extras"
        self.Author = "Krappa322"
        self.Github = "Krappa322/arcdps_unofficial_extras_releases"
        self.Path = "addons\\arcdps"
        self.SaveFileAs = "arcdps_unofficial_extras.dll"