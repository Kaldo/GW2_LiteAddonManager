import os
import Classes.helper as hp
import json
from AddonConfig.Addon import AddonStatus

class UserDataManager:
    """
    Save structure:
        ModManagerDataJson: {
            'FirstRun': True / False,
            'AddonInfo': {
                # 'ID' : {<addon info>}
                '1': {
                    'InstalledVersion': '1.0.0',
                    'IsDisabled': True
                }
            }
        }
    """
    def __init__(self, root, all_addons):
        self.root = root
        self.all_addons = all_addons
        self.ModManagerData = { 'FirstRun': True, 'AddonInfo': {} }
        self.StoragePath = "addons"
        self.FileName = "GW2-LAM-data.json"
        # create folder structure if missing
        path = os.path.join(self.root, self.StoragePath)
        if not os.path.exists(path):
            os.makedirs(path)
        else:
            self.load()

    def load(self):
        file_path = os.path.join(self.root, self.StoragePath, self.FileName)
        if not os.path.exists(file_path):
            return
        with open(file_path, 'r') as f:
            self.ModManagerData = json.load(f)
        for key, value in self.ModManagerData['AddonInfo'].items():
            addon = next(x for x in self.all_addons if str(x.ID) == key)
            if addon is not None:
                addon.InstalledVersion = value['InstalledVersion']
                addon.IsDisabled = value['IsDisabled']
                if addon.IsDisabled is True:
                    addon.AddonStatus = AddonStatus.DISABLED
                else:
                    addon.AddonStatus = AddonStatus.INSTALLED

    def save(self):
        self.ModManagerData.update({ 'FirstRun': False })
        file_path = os.path.join(self.root, self.StoragePath, self.FileName)
        with open(file_path, 'w') as f:
            json.dump(self.ModManagerData, f)

    def update_mod_info(self, id, installedVersion, isDisabled):
        if installedVersion is None and isDisabled is False:
            self.ModManagerData['AddonInfo'].pop(str(id), None)
        else:
            addonInfo = {
                'InstalledVersion': installedVersion,
                'IsDisabled': (isDisabled or False)
            }
            self.ModManagerData['AddonInfo'].update({ str(id): addonInfo })
        self.save()