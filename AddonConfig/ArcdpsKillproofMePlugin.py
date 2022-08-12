from .Addon import Addon

class ArcdpsKillproofMePlugin(Addon):
    def __init__(self):
        super(ArcdpsKillproofMePlugin, self).__init__()
        self.ID = 11
        self.Name = "ArcDPS killproof.me Plugin"
        self.Author = "knoxfighter"
        self.Github = "knoxfighter/arcdps-killproof.me-plugin"
        self.Path = "addons\\arcdps"
        self.SaveFileAs = "arcdps_killproof_me.dll"
        self.Description = """A Plugin for arcdps, that is loading killproof.me info and displaying it ingame."""