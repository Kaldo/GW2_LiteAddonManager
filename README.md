# Usage:

1. Download the Gw2ModManager.exe file and place it in your main "Guild Wars 2" installation folder, next to "Gw2-64.exe"
2. Run the tool
3. Run commands by typing the number and pressing enter

Every mod author has a different way of updating and organizing their mods. Support for new mods must be added manually. Github with tagged releases is the preferred way since then I can easily track versions through github api.

# Explanation of some functions:

    - Check for updates - updates the currently installed mods rows with the newest available version on their repo
    - Update all pending addons - reinstalls outdated mods with the newest version from repo
    - Remove addon - deletes the mod files from the game folder (only the originally installed files, not any other files that might have been created afterwards like logs)

# Developer stuff:

## requirements:

python -m pip install -U pip
pip install tqdm
pip install requests
pip install rich

## for packaging:

pip install pyinstaller
python -m PyInstaller main.py
