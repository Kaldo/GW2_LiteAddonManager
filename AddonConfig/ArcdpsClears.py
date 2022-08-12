from .Addon import Addon

class ArcdpsClears(Addon):
    def __init__(self):
        super(ArcdpsClears, self).__init__()
        self.ID = 6
        self.Name = "ArcDPS Clears"
        self.Author = "gw2scratch"
        self.Github = "gw2scratch/arcdps-clears"
        self.Path = "addons\\arcdps"
        self.SaveFileAs = "arcdps_clears.dll"