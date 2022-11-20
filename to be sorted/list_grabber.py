import json
from glob import glob

event_results = []

for f_name in glob('*.json'):
    if f_name in glob('decoded.*'):
        with open(f_name) as json_file:
            stat_file = json.load(json_file)
            sf = stat_file
            try:
                for event in sf["Events"]:
                    try:
                        if event["Num Outs During Play"] not in event_results:
                            event_results.append(event["Num Outs During Play"])
                    except KeyError:
                        continue
            except json.JSONDecodeError:
                continue

print(event_results)