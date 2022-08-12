import os
import sys
from .State import State
from AddonConfig.Addon import AddonStatus
from rich.progress import Progress
import subprocess
import helper as hp

class FirstRunState(State):
    def on_enter(self):
        hp.clear_screen()
        self.ssm.console.print("Welcome!\n")
        self.ssm.console.print("Disclaimer, still in beta, use at own risk, etc.")
        self.ssm.console.print("File must be placed in the root Guild Wars 2 folder.")
        self.ssm.console.print("If you understand and accept the risks, type [green]'yes'[/] and press enter to continue.\n")
        c = input("I understand and accept all risks: ")
        if c.lower() != "yes":
            sys.exit()

        # install mandatory addons
        mandatory_addons = list(filter(lambda x: (x.IsMandatory == True), self.ssm.all_addons))
        if len(mandatory_addons) > 0:
            # with Progress() as progress:
                # updating_task = progress.add_task("Installing mandatory plugins...", total=len(mandatory_addons))
            for addon in mandatory_addons:
                self.ssm.console.print("Installing % s" % addon.Name)
                addon.install(self.ssm, True)
                # os.system("cls")
                    # progress.update(updating_task, advance=1)

        # self.ssm.console.print("Since this is the first run of the manager, some mandatory plugins will be automatically installed.!\n")
        # self.ssm.console.print("They are required to make other plugins work properly.")
        # c = input(" ")
        # if c.lower() != "yes":
        #     exit()
        return MainMenuState(self.ssm)

    def on_command_given(self, command):
        if command == "Y" or command == "y" or command == "yes":
            return MainMenuState(self.ssm)
        else:
            sys.exit()

class MainMenuState(State):
    def on_enter(self):
        hp.clear_screen()

        # installed addons
        installed_addons = list(filter(lambda x: (x.AddonStatus == AddonStatus.PENDING_UPDATE 
            or x.AddonStatus == AddonStatus.INSTALLED), self.ssm.all_addons))
        self.print_select_addon_table("Installed addons", installed_addons)

        # commands
        command_table = self.get_command_grid_table()
        command_table.add_row("[magenta]number[/]: Select addon",   "",   "")
        command_table.add_row("c: Check for updates",   "a: Add a new addon",   "u. Update all pending addons")
        # command_table.add_row("4. Remove addon",        "5. Go to website",     "")
        command_table.add_row("[red]q[/]: Quit",        "[green]s[/]: Start Game",  "[yellow]?[/]: About")
        self.ssm.console.print(command_table)

        # TODO: remove all addons
        # TODO: disable all addons
        # TODO: enablea all addons
        # TODO: open addon info details
        # TODO: about/help section
        # TODO: reinstall all installed addons
        
        self.await_command()

    def on_command_given(self, command):
        if command.isdigit():
            installed_addons = list(filter(lambda x: (x.AddonStatus == AddonStatus.PENDING_UPDATE 
                or x.AddonStatus == AddonStatus.INSTALLED), self.ssm.all_addons))
            addon = next(x for x in installed_addons if str(x.Index) == str(command))
            AddonDetailsState(self.ssm, addon)
            self.on_enter()
        elif command == "c":
            # Check for updates
            with Progress() as progress:
                installed_addons = list(filter(lambda x: (x.AddonStatus == AddonStatus.PENDING_UPDATE 
                    or x.AddonStatus == AddonStatus.INSTALLED), self.ssm.all_addons))
                checking_task = progress.add_task("Checking...", total=len(installed_addons))
                for addon in installed_addons:
                    addon.check_for_updates()
                    progress.update(checking_task, advance=1)
            self.on_enter()
        elif command == "a":
            # Install specific addon
            return InstallMenuState(self.ssm)
        elif command == "u":
            # Update all pending addons
            pending = list(filter(lambda x: (x.AddonStatus == AddonStatus.PENDING_UPDATE), self.ssm.all_addons))
            if len(pending) > 0:
                with Progress() as progress:
                    updating_task = progress.add_task("Updating...", total=len(pending))
                    for addon in pending:
                        addon.install(self.ssm)
                        progress.update(updating_task, advance=1)
            self.on_enter()
        elif command == "4":
            return UninstallMenuState(self.ssm)
        elif command == "5":
            c = input("Which addon? ")
            if c.isdigit():
                installed_addons = list(filter(lambda x: (x.AddonStatus == AddonStatus.PENDING_UPDATE 
                    or x.AddonStatus == AddonStatus.INSTALLED), self.ssm.all_addons))
                addon = next(x for x in installed_addons if str(x.Index) == c)
                if addon is None:
                    self.ssm.console.print("Invalid number")
                else:
                    addon.open_website()
            self.on_enter()
        elif command == "q":
            return
        elif command == "s":
            os.chdir(self.ssm.root_path)
            subprocess.Popen("Gw2-64.exe")
            sys.exit()
        else:
            self.ssm.console.print("Unknown command")
            self.await_command()

class InstallMenuState(State):
    def on_enter(self):
        hp.clear_screen()

        # non installed addons
        uninstalled_addons = list(filter(lambda x: (x.AddonStatus == AddonStatus.NOT_INSTALLED 
            or x.AddonStatus == AddonStatus.UNREACHABLE), self.ssm.all_addons))
        self.print_select_addon_table("Available addons", uninstalled_addons)

        # commands
        self.ssm.console.print("Which addon do you want to install?")
        self.ssm.console.print("[yellow]q[/yellow]: Back")
        self.await_command()
    
    def on_command_given(self, command):
        if command == "q":
            return MainMenuState(self.ssm)
        elif command.isdigit():
            self.uninstall_addon(command)
            self.install_addon(command)
            return MainMenuState(self.ssm)
        else:
            self.ssm.console.print("Unknown command")
            return self.await_command()

    def install_addon(self, idx):
        uninstalled_addons = list(filter(lambda x: (x.AddonStatus == AddonStatus.NOT_INSTALLED 
            or x.AddonStatus == AddonStatus.UNREACHABLE), self.ssm.all_addons))
        addon = next(x for x in uninstalled_addons if str(x.Index) == idx)
        if addon is None:
            self.ssm.console.print("Invalid number")
            self.await_command()
        addon.install(self.ssm)

    def uninstall_addon(self, idx):
        uninstalled_addons = list(filter(lambda x: (x.AddonStatus == AddonStatus.NOT_INSTALLED 
            or x.AddonStatus == AddonStatus.UNREACHABLE), self.ssm.all_addons))
        addon = next(x for x in uninstalled_addons if str(x.Index) == idx)
        if addon is None:
            return
        addon.uninstall(self.ssm)

class UninstallMenuState(State):
    def on_enter(self):
        hp.clear_screen()

        # installed addons
        installed_addons = list(filter(lambda x: (x.AddonStatus == AddonStatus.PENDING_UPDATE 
            or x.AddonStatus == AddonStatus.INSTALLED), self.ssm.all_addons))
        self.print_select_addon_table("Installed addons", installed_addons)
        
        # commands
        self.ssm.console.print("Which addon do you want to remove?")
        self.ssm.console.print("[yellow]q[/yellow]: Back")
        self.await_command()
    
    def on_command_given(self, command):
        if command == "q":
            return MainMenuState(self.ssm)
        elif command.isdigit():
            return self.uninstall_addon(command)
        else:
            self.ssm.console.print("Unknown command")
            return self.await_command()

    def uninstall_addon(self, idx):
        installed_addons = list(filter(lambda x: (x.AddonStatus == AddonStatus.PENDING_UPDATE 
            or x.AddonStatus == AddonStatus.INSTALLED), self.ssm.all_addons))
        addon = next(x for x in installed_addons if str(x.Index) == idx)
        if addon is None:
            self.ssm.console.print("Invalid number")
            self.await_command()
        addon.uninstall(self.ssm)
        return MainMenuState(self.ssm)

class AddonDetailsState(State):
    def __init__(self, ssm, addon):
        self.addon = addon
        super(AddonDetailsState, self).__init__(ssm)

    def on_enter(self):
        hp.clear_screen()
        self.ssm.console.print("Name: " + self.addon.Name)
        self.ssm.console.print("Author: " + (self.addon.Author or '-'))
        self.ssm.console.print("Website: " + (self.addon.get_website_url() or '-'))
        status = (self.addon.AddonStatus.name or '-')
        if self.addon.AddonStatus == AddonStatus.INSTALLED:
            status = hp.tag_text(status, "green")
        elif self.addon.AddonStatus == AddonStatus.PENDING_UPDATE:
            status = hp.tag_text(status, "yellow")
        elif self.addon.AddonStatus == AddonStatus.UNREACHABLE:
            status = hp.tag_text(status, "red")
        if self.addon.IsMandatory is True:
            status += " [red]This is a core, mandatory mod and it should not be uninstalled."
        self.ssm.console.print("Status: " + status)
        self.ssm.console.print("Installed version: " + (self.addon.InstalledVersion or '-'))
        self.ssm.console.print("Available version: " + (self.addon.AvailableVersion or '-'))
        self.ssm.console.print("\n" + (self.addon.Description or '-') + "\n\n")
        
        # commands
        command_table = self.get_command_grid_table()
        command_table.add_row("1. Check for updates",   "2. Install")
        command_table.add_row("3. Open website",        "4. Uninstall")
        command_table.add_row("[red]q[/]: Back",        "")
        self.ssm.console.print(command_table)

        self.await_command()

    def on_command_given(self, command):
        if command == 'q':
            return
        elif command == '1':
            self.addon.check_for_updates()
        elif command == "2":
            if self.addon.IsMandatory is not True:
                self.addon.uninstall(self.ssm)
            self.addon.install(self.ssm)
        elif command == '3':
            self.addon.open_website()
        elif command == '4':
            if self.addon.IsMandatory is not True:
                self.addon.uninstall(self.ssm)
            else:
                self.ssm.console.print("Cannot uninstall this mod.")
        self.on_enter()