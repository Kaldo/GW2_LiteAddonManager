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
        self.Description = """The plugin shows a realtime list of failed mechanics for players. The mechanics are determined by the skill id of the attack a player/npc is hit by. It shows a timestamp in 'min:sec' since entering combat and 'X was hit by Y mechanic'.

This plugin is not intended to breed toxicity, but instead help show players mechanical areas where the players can improve. This is in the same way that arcdps shows how dps/boons could be improved."""