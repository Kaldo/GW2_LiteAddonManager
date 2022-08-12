import sys
from .MenuStates import MainMenuState
from .MenuStates import FirstRunState

class SimpleStateMachine(object):
    def __init__(self, root_path, console, all_addons, udm):
        self.root_path = root_path
        self.console = console
        self.all_addons = all_addons
        self.udm = udm

        if self.udm.ModManagerData['FirstRun'] == True:
            FirstRunState(self)
        else:
            MainMenuState(self)
        sys.exit()