from .Addon import Addon

class ArcdpsSquadReady(Addon):
    def __init__(self):
        super(ArcdpsSquadReady, self).__init__()
        self.ID = 3
        self.Name = "ArcDPS Squad Ready"
        self.Author = "cheahjs"
        self.Github = "cheahjs/arcdps-squad-ready-plugin"
        self.Path = "addons\\arcdps"
        self.SaveFileAs = "arcdps_squad_ready.dll"
        self.Description = """Plugin for arcdps to play audio files when a ready check has started and completed."""