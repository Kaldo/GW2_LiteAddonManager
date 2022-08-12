from .Addon import Addon

class ArcdpsScrollingCombatText(Addon):
    def __init__(self):
        super(ArcdpsScrollingCombatText, self).__init__()
        self.ID = 12
        self.Name = "ArcDPS Scrolling Combat Text"
        self.Author = "Artenuvielle"
        self.Github = "Artenuvielle/GW2-SCT"
        self.Path = "addons\\arcdps"
        self.SaveFileAs = "arcdps_sct.dll"