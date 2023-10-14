import sys
from .MenuStates import MainMenuState
from .MenuStates import FirstRunState
from .MenuStates import SelfUpdaterState

class SimpleStateMachine(object):
    def __init__(self, root_path, console, all_addons, udm, LAM_VERSION):
        self.root_path = root_path
        self.console = console
        self.all_addons = all_addons
        self.udm = udm
        self.LAM_VERSION = LAM_VERSION
        self.VersionText = None
        self.AvailableLamVersion = None

        # check for updates
        SelfUpdaterState(self)

        if self.udm.ModManagerData['FirstRun'] == True:
            FirstRunState(self)
        else:
            MainMenuState(self)
        sys.exit()