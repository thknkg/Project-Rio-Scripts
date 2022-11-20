import json
from glob import glob

def convert_json():
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
    return(all_files)

file_dict = convert_json()
game_info = {}
summary_def = {}
summary_off = {}
events = {}

for file_num, stats in file_dict.items():
    game_info = stats["game_info"]
    summary_def = stats["summary_def"]
    summary_off = stats["summary_off"]
    events = stats["events"]

# todo still need to iterate to add all of the stats together into a dict

def offensive_stats():
    for char, stat in summary_off.items():
        pa = stat["At Bats"] + stat["Walks (4 Balls)"] + stat["Walks (Hit)"] + stat["Sac Flys"]
        avg = round(stat["Hits"] / stat["At Bats"], 3)
        obp = round((stat["Hits"] + stat["Walks (4 Balls)"] + stat["Walks (Hit)"]) / pa, 3)
        slg = round((stat["Singles"] + (stat["Doubles"] * 2) + (stat["Triples"] * 3) + (stat["Homeruns"] * 4)) / stat["At Bats"], 3)
        ops = round(obp + slg, 3)
        print(char, "(" + str(pa) + " PA)", "/", "{:.3f}".format(avg), "/", "{:.3f}".format(obp), "/", "{:.3f}".format(slg), "/", "{:.3f}".format(ops))
offensive_stats()
