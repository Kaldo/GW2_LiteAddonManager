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
        self.Description = """This addon does nothing on its own. Instead, it provides other installed arcdps addons with additional information arcdps does not provide, namely:

    When players leave or join the party/squad
    What role a player has in the squad
    What subgroup a player is in
    If the player is ready or not (in a squad ready check)"""