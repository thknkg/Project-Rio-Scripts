import json
from glob import glob

"""
Search local MSSB statfiles and print specified event data
"""

# todo make it so user can give custom input

for f_name in glob('*.json'):
	if f_name in glob('decoded.*'):
		with open(f_name) as json_file:
			try:
				stat_file = json.load(json_file)
				for data in stat_file["Events"]:
					try:

						if data["Runner Batter"]["Runner Char Id"] == "Bowser":
							if data["Pitch"]["Contact"]["Type of Contact"] == "Sour - Left":
								if data["Pitch"]["Type of Swing"] == "Slap":
									# print(data)
									print(data["Pitch"]["Contact"]["Frame of Swing Upon Contact"], "/", data["Pitch"]["Contact"]["Input Direction - Push/Pull"], "/", data["Result of AB"],"/", data["Pitch"]["Contact"]["Contact Result - Secondary"])
					except KeyError:
						continue
			except json.JSONDecodeError:
				continue