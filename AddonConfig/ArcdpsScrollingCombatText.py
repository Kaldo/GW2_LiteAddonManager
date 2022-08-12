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
        self.Description = """This is an addon for arcdps by deltaconnected (https://www.deltaconnected.com/arcdps/) and adds a highly customizable floating and scrolling combat text beside the users character. Incoming damage is displayed on the left side, outgoing damage is displayed on the right side."""