import os
import sys
import Classes.helper as hp
from Classes.SimpleStateMachine import SimpleStateMachine
from Classes.UserDataManager import UserDataManager
from AddonConfig.ArcdpsD3d11 import ArcdpsD3d11
from AddonConfig.ArcdpsUnofficialExtras import ArcdpsUnofficialExtras
from AddonConfig.ArcdpsSquadReady import ArcdpsSquadReady
from AddonConfig.ArcdpsBoonTable import ArcdpsBoonTable
from AddonConfig.BlishHudArcdps import BlishHudArcdps
from AddonConfig.ArcdpsClears import ArcdpsClears
from AddonConfig.ArcdpsMechanicsLog import ArcdpsMechanicsLog
from AddonConfig.GW2Radial import GW2Radial
from AddonConfig.ArcdpsFoodReminder import ArcdpsFoodReminder
from AddonConfig.ArcdpsHealingStats import ArcdpsHealingStats
from AddonConfig.ArcdpsKillproofMePlugin import ArcdpsKillproofMePlugin
from AddonConfig.ArcdpsScrollingCombatText import ArcdpsScrollingCombatText
from AddonConfig.ArcdpsSquadRoleTracker import ArcdpsSquadRoleTracker
# from AddonConfig.ArcdpsUploader import ArcdpsUploader
from AddonConfig.GW2AddonLoader import GW2AddonLoader
from AddonConfig.GW2AddonD3D9Wrapper import GW2AddonD3D9Wrapper

LAM_VERSION = "v0.6"
all_addons = [
    GW2AddonLoader(), # 14
    GW2AddonD3D9Wrapper(), # 15
    ArcdpsD3d11(), # 1
    ArcdpsUnofficialExtras(), # 2
    ArcdpsBoonTable(), # 4
    ArcdpsClears(), # 6
    ArcdpsFoodReminder(), # 9
    ArcdpsHealingStats(), # 10
    ArcdpsKillproofMePlugin(), # 11
    ArcdpsMechanicsLog(), # 7
    ArcdpsScrollingCombatText(), #12
    ArcdpsSquadReady(), # 3
    ArcdpsSquadRoleTracker(), # 16
    # ArcdpsUploader(), # 13
    BlishHudArcdps(), # 5
    GW2Radial(), # 8
]

hp.clear_screen()
console = hp.setup_console()
try:
    # Check if executable is in good location
    if not os.path.isdir('bin64') or not os.path.exists('Gw2-64.exe'):
        console.print('[bold red]This executable should be placed in the same directory where Gw2-64.exe is located.[/]\n')    
        c = input("Press enter to continue...")
        sys.exit()

    # get current exe location
    def get_application_path():
        if getattr(sys, 'frozen', False):
            return sys.executable.rsplit('\\', 1)[0]
        else:
            return os.path.dirname(os.path.abspath(__file__))
    application_path = get_application_path()

    # start app
    udm = UserDataManager(application_path, all_addons)
    ssm = SimpleStateMachine(application_path, console, all_addons, udm, LAM_VERSION)
except Exception as e:
    print(e)
    console.print('\n[bold red]Unhandled exception, please report the issue.[/]\n')    
    c = input("Press enter to exit...")
