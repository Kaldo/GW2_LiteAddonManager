from .Addon import Addon

class ArcdpsHealingStats(Addon):
    def __init__(self):
        super(ArcdpsHealingStats, self).__init__()
        self.ID = 10
        self.Name = "ArcDPS Healing Stats"
        self.Author = "Krappa322"
        self.Github = "Krappa322/arcdps_healing_stats"
        self.Path = "addons\\arcdps"
        self.SaveFileAs = "arcdps_healing_stats.dll"