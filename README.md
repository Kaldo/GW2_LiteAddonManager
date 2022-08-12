# Usage:

1. To eliminate the chance of conflicts or redundant files, it is best to remove all existing mods before trying to manage them with LAM
2. Download the GW2-LAM.exe file from https://github.com/Kaldo/GW2_LiteAddonManager/releases and place it in your main "Guild Wars 2" installation folder, next to "Gw2-64.exe"
3. Run the tool
4. First time setup will install the core prerequisites automatically. Please do not remove them, they are required for other addons to work properly
5. Commands for each screen are listed on that screen, type the number or the letter and press enter to execute it

Every mod author has a different way of updating and organizing their mods. Support for new mods must be added manually. Github with tagged releases is the preferred way since then I can easily track versions through github api, but manual implementations are possible too.

# Explanation of some functions:

    - Check for updates - updates the currently installed mods rows with the newest available version on their repo
    - Update all pending addons - reinstalls outdated mods with the newest version from repo
    - Remove addon - deletes the mod files from the game folder (only the originally installed files, not any other files that might have been created afterwards like logs)

# Roadmap for potential future updates:

- automatic self-updating for GW2-LAM
- ability to temporarily disable installed mods (without uninstalling them)
- figure out how to render it in a prettier console
- linux support? maybe?

# Developer stuff, if you want to build it yourself:

## requirements:

python -m pip install -U pip
pip install tqdm
pip install requests
pip install rich

## for packaging:

pip install pyinstaller
pyInstaller main.py --onefile
