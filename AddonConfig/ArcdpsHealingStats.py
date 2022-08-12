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
        self.Description = """Show healing statistics based on your local stats (i.e. your own healing output).

This includes outgoing healing per agent and per skill, as well as filtering to only include your own subgroup/squad or to exclude minions. Format of the window title and contents are fully configurable and windows can be configured to show different data (targets healed, skills used to heal, total healing).

If live stats sharing is enabled, this addon also allows you to see other players in your squads healing stats (and them to see yours)

Also logs healing to the arcdps evtc, allowing evtc parsers to show healing stats."""