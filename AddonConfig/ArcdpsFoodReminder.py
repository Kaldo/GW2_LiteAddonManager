from .Addon import Addon

class ArcdpsFoodReminder(Addon):
    def __init__(self):
        super(ArcdpsFoodReminder, self).__init__()
        self.ID = 9
        self.Name = "ArcDPS Food Reminder"
        self.Author = "Zerthox"
        self.Github = "Zerthox/arcdps-food-reminder"
        self.Path = "addons\\arcdps"
        self.SaveFileAs = "arcdps_food_reminder.dll"