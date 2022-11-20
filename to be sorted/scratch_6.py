import json
from json import JSONEncoder
from glob import glob

class StatFile(JSONEncoder):
    def default(self, o):
        return o.__dict__



for f_name in glob('*.json'):
    if f_name in glob('decoded.*'):
        with open(f_name) as json_file:
                stat_file = json.load(json_file)
                sf = stat_file


