from .Addon import Addon

class ArcdpsBoonTable(Addon):
    def __init__(self):
        super(ArcdpsBoonTable, self).__init__()
        self.ID = 4
        self.Name = "ArcDPS Boon Table"
        self.Author = "knoxfighter"
        self.Github = "knoxfighter/GW2-ArcDPS-Boon-Table"
        self.Path = "addons\\arcdps"
        self.SaveFileAs = "d3d9_arcdps_table.dll"