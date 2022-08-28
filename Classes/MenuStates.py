import os
import sys
from .State import State
from AddonConfig.Addon import AddonStatus
from rich.progress import Progress
import subprocess
import Classes.helper as hp
from rich.panel import Panel

class FirstRunState(State):
    def on_enter(self):
        hp.clear_screen()
        self.ssm.console.print("Welcome!\n")
        self.ssm.console.print("Disclaimer - tools is still in early development. Use at own risk, create backups of your addons if you don't want to accidentally lose some settings.")
        self.ssm.console.print("This executable file must be placed in the root Guild Wars 2 folder, next to the Gw2-64.exe file.")
        self.ssm.console.print("If you manually change files in the folders LAM will not know about it. Either make changes through the manager only, or make sure to remove/add addons to LAM as well.")
        self.ssm.console.print("\nIf you understand and accept the risks, type [green]'yes'[/] and press enter to continue.\n")
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
            or x.AddonStatus == AddonStatus.INSTALLED
            or x.AddonStatus == AddonStatus.DISABLED), self.ssm.all_addons))
        self.print_select_addon_table("Installed addons", installed_addons)

        # commands
        command_table = self.get_command_grid_table()
        command_table.add_row("[magenta]Index[/]: Select addon", "", "")
        command_table.add_row("[yellow]C[/]: Check for updates", "[green]A[/]: Add a new addon", "[cyan]U[/]: Update all pending addons")
        # command_table.add_row("4. Remove addon",        "5. Go to website",     "")
        command_table.add_row("[cyan]B[/]: Bulk actions", "[yellow]?[/]: About LAM", "")
        command_table.add_row("[red]Q[/]: Quit",        "[green]S[/]: Start GW2",  "")
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
                or x.AddonStatus == AddonStatus.INSTALLED
                or x.AddonStatus == AddonStatus.DISABLED), self.ssm.all_addons))
            try:
                addon = next(x for x in installed_addons if str(x.Index) == str(command))
            except StopIteration:
                self.ssm.console.print("Invalid number.")
                return self.await_command()
            AddonDetailsState(self.ssm, addon)
            self.on_enter()
        elif command.lower() == "c":
            # Check for updates
            with Progress() as progress:
                installed_addons = list(filter(lambda x: (x.AddonStatus == AddonStatus.PENDING_UPDATE 
                    or x.AddonStatus == AddonStatus.INSTALLED
                    or x.AddonStatus == AddonStatus.DISABLED), self.ssm.all_addons))
                checking_task = progress.add_task("Checking...", total=len(installed_addons))
                for addon in installed_addons:
                    addon.check_for_updates()
                    progress.update(checking_task, advance=1)
            self.on_enter()
        elif command.lower() == "a":
            # Install specific addon
            InstallMenuState(self.ssm)
            self.on_enter()
        elif command.lower() == "u":
            # Update all pending addons
            pending = list(filter(lambda x: (x.AddonStatus == AddonStatus.PENDING_UPDATE), self.ssm.all_addons))
            if len(pending) > 0:
                with Progress() as progress:
                    updating_task = progress.add_task("Updating...", total=len(pending))
                    for addon in pending:
                        addon.install(self.ssm)
                        progress.update(updating_task, advance=1)
            self.on_enter()
        elif command.lower() == "q":
            return
        elif command.lower() == "s":
            os.chdir(self.ssm.root_path)
            subprocess.Popen("Gw2-64.exe")
            sys.exit()
        elif command.lower() == "b":
            self.ssm.console.print("Unknown command")
            self.await_command()
        elif command == "?":
            AboutLamState(self.ssm)
            self.on_enter()
        else:
            self.ssm.console.print("Unknown command")
            self.await_command()

class InstallMenuState(State):
    def on_enter(self):
        hp.clear_screen()

        # non installed addons
        uninstalled_addons = list(filter(lambda x: (x.AddonStatus == AddonStatus.NOT_INSTALLED 
            or x.AddonStatus == AddonStatus.UNREACHABLE
            or x.AddonStatus == AddonStatus.DISABLED), self.ssm.all_addons))
        self.print_select_addon_table("Available addons", uninstalled_addons)

        # commands
        self.ssm.console.print("[magenta]Index[/]: Select addon")
        self.ssm.console.print("[yellow]Q[/yellow]: Back")
        self.await_command()
    
    def on_command_given(self, command):
        if command.isdigit():
            uninstalled_addons = list(filter(lambda x: (x.AddonStatus == AddonStatus.NOT_INSTALLED 
                or x.AddonStatus == AddonStatus.UNREACHABLE
                or x.AddonStatus == AddonStatus.DISABLED), self.ssm.all_addons))
            try:
                addon = next(x for x in uninstalled_addons if str(x.Index) == str(command))
            except StopIteration:
                self.ssm.console.print("Invalid number.")
                return self.await_command()
            AddonDetailsState(self.ssm, addon)
            return self.on_enter()
        elif command.lower() == "q":
            return
        else:
            self.ssm.console.print("Unknown command")
            return self.await_command()

class AddonDetailsState(State):
    def __init__(self, ssm, addon):
        self.addon = addon
        super(AddonDetailsState, self).__init__(ssm)

    def on_enter(self):
        hp.clear_screen()

        status = (self.addon.AddonStatus.name or '-')
        if self.addon.AddonStatus == AddonStatus.INSTALLED:
            status = hp.tag_text(status, "green")
        elif self.addon.AddonStatus == AddonStatus.PENDING_UPDATE:
            status = hp.tag_text(status, "yellow")
        elif self.addon.AddonStatus == AddonStatus.UNREACHABLE:
            status = hp.tag_text(status, "red")
        if self.addon.IsMandatory is True:
            status += "[red]*\n  This is a core, mandatory mod.[/]"

        desc = '' if self.addon.Description is None else f"\n\n{self.addon.Description}"

        text = f"""Name: [cyan]{self.addon.Name}[/]
Author: {(self.addon.Author or '-')}
Website: {(self.addon.get_website_url() or '-')}
Status: {status}
Installed version: {(self.addon.InstalledVersion or '-')}
Available version: {(self.addon.AvailableVersion or '-')}{desc}"""
        self.ssm.console.print(Panel(text, expand=False))
        self.ssm.console.print()

        # commands
        command_table = self.get_command_grid_table()
        command_table.add_row("[yellow]C[/]: Check for updates",   "[green]I[/]: Install", "[magenta]U[/]: Uninstall")
        command_table.add_row("[red]Q[/]: Back", "[cyan]W[/]: Open website", "[magenta]D[/]: Disable")
        self.ssm.console.print(command_table)

        self.await_command()

    def on_command_given(self, command):
        if command.lower() == 'q':
            return
        elif command.lower() == 'c':
            self.addon.check_for_updates()
            self.on_enter()
        elif command.lower() == "i":
            if self.addon.IsMandatory is not True:
                self.addon.uninstall(self.ssm)
            self.addon.install(self.ssm)
            self.on_enter()
        elif command.lower() == 'w':
            self.addon.open_website()
            self.on_enter()
        elif command.lower() == 'u':
            if self.addon.IsMandatory is not True:
                self.addon.uninstall(self.ssm)
                self.on_enter()
            else:
                self.ssm.console.print("Cannot uninstall this mod.")
                return self.await_command()
        elif command.lower() == 'd':
            if self.addon.IsMandatory is not True:
                self.addon.uninstall(self.ssm, disable=True)
                self.on_enter()
            else:
                self.ssm.console.print("Cannot disable this mod.")
                return self.await_command()
        else:
            self.ssm.console.print("Unknown command.")
            return self.await_command()

class BulkActionsState(State):
    def __init__(self, ssm):
        super(BulkActionsState, self).__init__(ssm)
    
    def on_enter(self):
        hp.clear_screen()
        # installed addons
        installed_addons = list(filter(lambda x: (x.AddonStatus == AddonStatus.PENDING_UPDATE 
            or x.AddonStatus == AddonStatus.INSTALLED), self.ssm.all_addons))
        self.print_select_addon_table("Installed addons", installed_addons)

        # commands
        command_table = self.get_command_grid_table()
        command_table.add_row("[magenta]Index[/]: Select addon", "", "")
        command_table.add_row("[green]E[/]: Enable all disabled addons", "[blue]D[/]: Disable all enabled addons")
        command_table.add_row("[magenta]R[/]: Remove all addons", "[blue]U[/]: Update all pending addons")
        command_table.add_row("[red]Q[/]: Back")
        self.ssm.console.print(command_table)
        self.await_command()

    def on_command_given(self, command):
        if command.isdigit():
            installed_addons = list(filter(lambda x: (x.AddonStatus == AddonStatus.PENDING_UPDATE 
                or x.AddonStatus == AddonStatus.INSTALLED), self.ssm.all_addons))
            try:
                addon = next(x for x in installed_addons if str(x.Index) == str(command))
            except StopIteration:
                self.ssm.console.print("Invalid number.")
                return self.await_command()
            AddonDetailsState(self.ssm, addon)
            self.on_enter()
        if command.lower() == 'q':
            return
        elif command.lower() == 'e':
            # TODO: enable all disabled
            return
        elif command.lower() == 'd':
            # TODO: disable all enabled, except mandatory
            return
        elif command.lower() == 'u':
            # TODO: uninstall all installed, except mandatory
            return
        else:
            self.ssm.console.print("Unknown command.")
            return self.await_command()

class SelfUpdaterState(State):
    def __init__(self, ssm):
        super(SelfUpdaterState, self).__init__(ssm)

    def on_enter(self):
        self.ssm.console.print("Checking for new GW2 LAM updates...")
        ri = hp.get_github_latest_release_info("Kaldo/GW2_LiteAddonManager")
        if ri is None:
            self.ssm.console.print("Could not fetch update info. Please consider manually checking if a new version is available.")
            self.ssm.VersionText = f"[red]{self.ssm.LAM_VERSION}[/] [red](update unavailable)[/]"
            input("Press enter to continue...")
            return
        if ri['version'] == self.ssm.LAM_VERSION:
            self.ssm.VersionText = f"[white]{self.ssm.LAM_VERSION}[/]"
            return
        else:
            self.ssm.VersionText = f"[yellow]{self.ssm.LAM_VERSION}[/] [yellow](update available)[/]"
            self.ssm.console.print("A new update for GW2 LAM is available. Do you want it to install automatically now?")
            c = input("yes / no ?")
            if c.lower() == "yes":
                # automatic install process
                self.ssm.console.print("Installing update... \nGW2 LAM will restart automatically when it is done.")

class AboutLamState(State):
    def __init__(self, ssm, addon):
        self.addon = addon
        super(AboutLamState, self).__init__(ssm)

    def on_enter(self):
        hp.clear_screen()

        text = f"""Name: [cyan]GW2 Lite Addon Manager[/]
Author: Kaldo
Website: https://github.com/Kaldo/GW2_LiteAddonManager
Installed version: {(self.ssm.LAM_VERSION or '-')}
Available version: {(self.addon.AvailableVersion or '-')}

GW2 LAM is an unofficial Lightweight Addon Manager for Guild Wars 2 using a console terminal. With only a few key presses you can check out and install any of the supported addons, get notified if there is a new version available and easily disable or uninstall them at any point."""
        self.ssm.console.print(Panel(text, expand=False))
        self.ssm.console.print()

        # commands
        command_table = self.get_command_grid_table()
        command_table.add_row("[red]Q[/]: Back", "[cyan]W[/]: Open website")
        self.ssm.console.print(command_table)

        self.await_command()

    def on_command_given(self, command):
        if command.lower() == 'q':
            return
        elif command.lower() == 'w':
            self.addon.open_website()
            self.on_enter()
        else:
            self.ssm.console.print("Unknown command.")
            return self.await_command()                