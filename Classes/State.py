import os
from rich.table import Table
from rich.rule import Rule
from rich import box
from AddonConfig.Addon import AddonStatus
from rich.text import Text
import Classes.helper as hp

class State:
    def __init__(self, ssm):
        self.ssm = ssm
        self.on_enter()

    def on_enter(self):
        os.system("cls")
        self.print_addon_table()

    def await_command(self):
        c = input("\nCommand: ")
        self.on_command_given(c)

    def on_command_given(self, command):
        pass

    def print_addon_table(self):
        self.print_select_addon_table("Current addons", self.ssm.all_addons)

    def print_select_addon_table(self, title, addons):
        title = f"[bold green]GW2 Lite Addon Manager[/bold green] {self.ssm.VersionText}"
        self.ssm.console.print(Rule(title))

        table = Table(safe_box=True, box = box.SIMPLE, show_footer = True, expand = True)

        table.add_column("Index", justify="right", no_wrap=True)
        table.add_column("Name", no_wrap=True)
        table.add_column("Author",  style="cyan", no_wrap=True)
        table.add_column("Status", justify="left")
        table.add_column("Current version", justify="right")
        table.add_column("Available version", justify="right")

        idx = 1
        for addon in addons:
            # format Index
            index = hp.tag_text("% s." % idx, "magenta")

            # format name
            name = hp.tag_text(addon.Name, "cyan")
            if addon.Github is not None:
                name = hp.tag_text(name, "link=https://github.com/% s" % addon.Github)

            # format status
            status = addon.AddonStatus.name
            if addon.IsMandatory == True:
                status = f"{status}*"
            if addon.AddonStatus == AddonStatus.INSTALLED:
                status = hp.tag_text(status, "green")
            elif addon.AddonStatus == AddonStatus.PENDING_UPDATE:
                status = hp.tag_text(status, "yellow")
            elif addon.AddonStatus == AddonStatus.DISABLED:
                status = hp.tag_text(status, "magenta")

            # format cu. Version
            cuVersion = "-"
            if addon.InstalledVersion is not None:
                 cuVersion = str(addon.InstalledVersion)[0:10]
            if addon.AddonStatus == AddonStatus.INSTALLED:
                cuVersion = hp.tag_text(cuVersion, "green")
            elif addon.AddonStatus == AddonStatus.PENDING_UPDATE:
                cuVersion = hp.tag_text(cuVersion, "yellow")
            elif addon.AddonStatus == AddonStatus.DISABLED:
                cuVersion = hp.tag_text(cuVersion, "magenta")

            # format av. version
            avVersion = "-"
            if addon.AvailableVersion is not None:
                avVersion = str(addon.AvailableVersion)[0:10]
            if addon.AvailableVersion == AddonStatus.UNREACHABLE.name:
                avVersion = hp.tag_text('N/A', "red")            

            table.add_row(index, name, addon.Author, status, cuVersion, avVersion)
            addon.Index = idx
            idx += 1

        self.ssm.console.print(table)

    def get_command_grid_table(self):
        table = Table(safe_box=True,
            box = None,
            show_edge=False,
            show_lines=False,
            show_header=False,
            expand=False)
        return table
