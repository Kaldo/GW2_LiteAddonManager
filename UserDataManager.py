import os
import helper as hp
import json
from AddonConfig.Addon import AddonStatus

class UserDataManager:
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
                addon.InstalledVersion = value
                addon.AddonStatus = AddonStatus.INSTALLED

    def save(self):
        self.ModManagerData.update({ 'FirstRun': False })
        file_path = os.path.join(self.root, self.StoragePath, self.FileName)
        with open(file_path, 'w') as f:
            json.dump(self.ModManagerData, f)

    def set_version(self, id, installedVersion):
        if installedVersion is None:
            self.ModManagerData['AddonInfo'].pop(str(id), None)
        else:
            self.ModManagerData['AddonInfo'].update({ str(id): str(installedVersion) })
        self.save()