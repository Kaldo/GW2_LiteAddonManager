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
        self.Description = """A plugin for arcdps which adds a window for quickly checking your current weekly clears in the game.

This plugin uses the official Guild Wars 2 API to get the clear data, you will need an API key (with access to account and progression).

The plugin uses no actual arcdps combat data, so it is the same as your typical overlay program – no need to worry about breaking any rules."""