from .Addon import Addon

class ArcdpsBoonTable(Addon):
    def __init__(self):
        super(ArcdpsBoonTable, self).__init__()
        self.ID = 4
        self.Name = "ArcDPS Boon Table"
        self.Author = "knoxfighter"
        self.Github = "knoxfighter/GW2-ArcDPS-Boon-Table"
        self.Path = "addons\\arcdps"
        self.SaveFileAs = "d3d9_arcdps_table.dll"
        self.Description = """Alt+Shift+B (overwrites Arc's default boon table hotkey) or checkbox in the arc options

Right-click for options to change column visible and other settings.
Table columns can be reordered by dragging the column header.
Sort by column by clicking on the header, it is sorted by character name by default."""