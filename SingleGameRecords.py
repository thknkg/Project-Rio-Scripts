import json
from glob import glob

"""
Script for parsing local MSSB statfiles and outputting results that are among the best for the user.
"""

# todo implement a loop that iterates until the highest value has been reached instead of arbitrarily assigning values
# char = input("Input character: ")
user = "MORI"
for f_name in glob('*.json'):
	if f_name in glob('decoded.*'):
		with open(f_name) as json_file:

			try:
				stat_file = json.load(json_file)
				for char in stat_file["Character Game Stats"].values():
					if stat_file["Ranked"] == 1:
						if (char["Team"] == "1" and stat_file["Away Player"] == user) or (char["Team"] == "0" and stat_file["Home Player"] == user) and char["Superstar"] == 0:
							if char["Offensive Stats"]["Hits"] >= 5:
								print(char["CharID"]+" Hits", char["Offensive Stats"]["Hits"])
							if char["Offensive Stats"]["Doubles"] >= 4:
								print(char["CharID"]+" Doubles", char["Offensive Stats"]["Doubles"])
							if char["Offensive Stats"]["Triples"] >= 2:
								print(char["CharID"]+" Triples", char["Offensive Stats"]["Triples"])
							if char["Offensive Stats"]["Homeruns"] >= 3:
								print(char["CharID"]+" Homeruns", char["Offensive Stats"]["Homeruns"])
							if char["Offensive Stats"]["RBI"] >= 8:
								print(char["CharID"]+" RBI", char["Offensive Stats"]["RBI"])
							if char["Offensive Stats"]["Bases Stolen"] >= 2:
								print(char["CharID"]+" SB", char["Offensive Stats"]["Bases Stolen"])
							if char["Defensive Stats"]["Strikeouts"] >= 15:
								print(char["CharID"]+" K", char["Defensive Stats"]["Strikeouts"])
							if char["Defensive Stats"]["Big Plays"] >= 4:
								print(char["CharID"] + " Big Plays", char["Defensive Stats"]["Big Plays"])
			# 	for event in stat_file["Events"]:
			# 		try:
			# 			if event["Runner Batter"]["Runner Char Id"] == char:
			# 			#if data["Pitch"]["Contact"]["Contact Result - Primary"] == "Fair" and data["Pitch"]["Contact"]["Contact Result - Secondary"] == "foul":
			# 				print(event["Event Num"], event["Result of AB"], "/", event["Pitch"]["Contact"]["Type of Contact"], "/", event["Pitch"]["Contact"]["Frame of Swing Upon Contact"], "/", event["Pitch"]["Contact"]["Contact Result - Primary"],"/", event["Pitch"]["Contact"]["Contact Result - Secondary"], "/", event["Pitch"]["Contact"]["Input Direction - Stick"])
			# 			else:
			# 				pass
			# 		except KeyError:
			# 			pass
			except json.JSONDecodeError:
			 	continue