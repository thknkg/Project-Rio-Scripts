import json
from glob import glob

 # for opening local file for easy testing
all_files = {}
file_count = 0
for f_name in glob('*.json'):
    if f_name in glob('decoded.*'):
        with open(f_name) as json_file:
            stat_file = json.load(json_file)
            sf = stat_file
            summary_off = {}
            summary_def = {}
            game_information = {}

            # automate creation of variables for statfiles
            count = 0

            # overall stat file dictionary
            stat_file_dict = {}
            for key, value in sf.items():
                stat_file_dict[key] = value

                # create non-character, non-event stat dictionary (game info, date, etc.)
                if count < 16:
                    game_information[key] = value
                count += 1

            # defining variables for summary and event stats for easier access
            summary_stats = stat_file_dict["Character Game Stats"]
            for char in summary_stats.values():
                summary_def[char["CharID"]] = char["Defensive Stats"]
                summary_off[char["CharID"]] = char["Offensive Stats"]
            events = stat_file_dict["Events"]

    # create a dictionary to return
dict_for_return = {}
dict_for_return["game_info"] = game_information
dict_for_return["summary_def"] = summary_def
dict_for_return["summary_off"] = summary_off
dict_for_return["events"] = events
file_count += 1
all_files[file_count] = dict_for_return

game_info = dict_for_return["game_info"]
summary_def = dict_for_return["summary_def"]
summary_off = dict_for_return["summary_off"]
events = dict_for_return["events"]