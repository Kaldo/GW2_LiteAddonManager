# About

GW2 LAM is an unofficial Lightweight Addon Manager for Guild Wars 2 using a console terminal. With only a few key presses you can check out and install any of the supported addons, get notified if there is a new version available and easily disable or uninstall them at any point.

![image](https://user-images.githubusercontent.com/3905101/184853368-3b8405b6-1893-4b8c-bdb1-c62817439818.png)

# How to use:

1. To eliminate the chance of conflicts or redundant files it is best to remove all existing mods before trying to manage them with LAM
2. Download the GW2-LAM.exe file from https://github.com/Kaldo/GW2_LiteAddonManager/releases and place it in your main "Guild Wars 2" installation folder, next to "Gw2-64.exe"
3. Run the tool. If you want it to look nicer, run it in a more modern terminal like Windows Terminal instead of the default windows console
4. Commands for each screen are listed on that screen, type the number or the letter and press enter to execute it

![image](https://user-images.githubusercontent.com/3905101/184853497-3f181d5b-91e5-42c2-a61a-ec12e16a6dc2.png)

Every mod author has a different way of updating and organizing their mods. Support for new mods must be added manually. Github with tagged releases is the preferred way since then I can easily track versions through github api, but manual implementations are possible too.

GW2 LAM is using https://github.com/gw2-addon-loader/loader-core as a core to enable chain loading of addons and all mods are automatically organized according to its desired structure. Because of that, loader-core and d3d9wrapper are mandatory installs for LAM to function properly and should not be removed. They will be automatically installed when GW2 LAM is started for the first time.

# Explanation of some functions:

    - Check for updates - updates the currently installed mods rows with the newest available version on their repo
    - Update all pending addons - reinstalls outdated mods with the newest version from repo
    - Remove addon - deletes the mod files from the game folder (only the originally installed files, not any other files that might have been created afterwards like logs)
    - Disable - removes mods but keeps them in the installed list as 'DISABLED' so they can be easily re-enabled later

# Roadmap for potential future updates:

- automatic self-updating for GW2-LAM
- ability to temporarily disable installed mods (without uninstalling them)
- headless option for auto-updating of addons in the background
- figure out how to render it in a prettier console
- linux support? maybe?
- figure out a punny acronym like LAMB, LAMP, LAME, GLAM, BLAM or CLAM

# Developer stuff, if you want to build it yourself:

## requirements:

developed with python 3.10.6  
python -m pip install -U pip  
pip install tqdm  
pip install requests  
pip install rich  

## for packaging:

pip install pyinstaller  
pyInstaller main.py --onefile  

## adding support for other addons

I will (eventually) accept requests and pull requests to add support for other github-based mods after I thoroughly test them myself. Only addons that have existed and have been maintained for a while though.

Non-github mods that require more customized implementation might take a bit longer since they are a bit riskier and harder to maintain - checking versions, unzipping files, resolving multiple files is doable but gets a bit more complicated.
