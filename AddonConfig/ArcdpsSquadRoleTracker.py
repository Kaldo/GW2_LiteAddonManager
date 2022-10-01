from .Addon import Addon

class ArcdpsSquadRoleTracker(Addon):
    def __init__(self):
        super(ArcdpsSquadRoleTracker, self).__init__()
        self.ID = 16
        self.Name = "ArcDPS Squad Role Manager"
        self.Author = "cheahjs"
        self.Github = "RaidcoreGG/GW2-CommandersToolkit"
        self.Path = "addons\\arcdps"
        self.SaveFileAs = "squadmanager.dll"
        self.Description = """A simple arcdps module that tracks squad members, so that you can check if someone left the party what they were responsible for."""