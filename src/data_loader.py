import json


class DataLoader:
    def __init__(self, config):
        self.base_path = config['base_path']
        self.language = config['language']

    def load(self, s):
        with open("%s/%s/%s.json" % (self.base_path, self.language, s), encoding='utf-8') as json_data_file:
            return json.load(json_data_file)
