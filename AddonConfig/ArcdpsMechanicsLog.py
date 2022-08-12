from .Addon import Addon

class ArcdpsMechanicsLog(Addon):
    def __init__(self):
        super(ArcdpsMechanicsLog, self).__init__()
        self.ID = 7
        self.Name = "ArcDPS Mechanics Log"
        self.Author = "knoxfighter"
        self.Github = "knoxfighter/GW2-ArcDPS-Mechanics-Log"
        self.Path = "addons\\arcdps"
        self.SaveFileAs = "arcdps_squad_ready.dll"