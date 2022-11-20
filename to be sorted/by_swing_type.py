import requests


url = 'https://projectrio-api-1.api.projectrio.app/detailed_stats/?tag=Normal&exclude_pitching=1&exclude_misc=1&exclude_fielding=1&by_swing=1&tag=ranked'




print("Enter name of character (blank for all stats):")
char = input()
print("Enter '0' for bunt; '1' for none; '2 for slap'; '3 for charge'; '4 for star':")
hit_type = int(input())

if hit_type == 0:
    swing = "Bunt"
if hit_type == 1:
    swing = "None"
if hit_type == 2:
    swing = "Slap"
if hit_type == 3:
    swing = "Charge"
if hit_type == 4:
    swing = "Star"

if char != "":
    url += "&by_char=1"

total_response = requests.get(url).json()
total_char_response = requests.get(url + "&by_user=1").json()

user_dict = {}

overall = {}
if char == "":
    overall = total_response["Stats"]["Batting"][swing]
else:
    overall = total_response["Stats"][char]["Batting"][swing]
singles = overall["singles"]
doubles = overall["doubles"]
triples = overall["triples"]
homeruns = overall["homeruns"]
plate_appearances = overall["plate_appearances"]
extra_base_hits = str(round((doubles + triples + homeruns) / (singles + doubles + triples + homeruns) * 100, 1))
perfect_hits = overall["perfect_hits"]
sour_hits = overall["sour_hits"]
nice_hits = overall["nice_hits"]
contact_rates = {"sour": sour_hits / (sour_hits + nice_hits + perfect_hits),
                 "nice": nice_hits / (sour_hits + nice_hits + perfect_hits),
                 "perfect": perfect_hits / (sour_hits + nice_hits + perfect_hits)}
sour = contact_rates["sour"]
nice = contact_rates["nice"]
perfect = contact_rates["perfect"]

print(f'{char}',"-", "Overall:", plate_appearances, "PA /", round((singles + doubles + triples + homeruns) / plate_appearances, 3), "AVG / ", extra_base_hits + "% extra base hits\n")
print(str(round(sour * 100, 1)) + "% sour / " + str(round(nice * 100, 1)) + "% nice / " + str(round(perfect * 100, 1)) + "% perfect\n")


for user in total_char_response["Stats"]:
    # todo
    stats = {}
    try:
        if char == "":
            stats = total_char_response["Stats"][user]["Batting"][swing]
        elif char in total_char_response["Stats"][user]:
            stats = total_char_response["Stats"][user][char]["Batting"][swing]
        else:
            continue

        singles = stats["singles"]
        doubles = stats["doubles"]
        triples = stats["triples"]
        homeruns = stats["homeruns"]
        rbi = stats["rbi"]
        plate_appearances = stats["plate_appearances"]

        strikeouts = stats["strikeouts"]
        multi_out = stats["multi_out"]
        outs = stats["outs"]
        total_outs = strikeouts + multi_out + outs

        perfect_hits = stats["perfect_hits"]
        sour_hits = stats["sour_hits"]
        nice_hits = stats["nice_hits"]
        try:
            extra_base_hits = round((doubles + triples + homeruns) / (singles + doubles + triples + homeruns) * 100, 1)
            contact_rates = {"sour": sour_hits / (sour_hits + nice_hits + perfect_hits),
                             "nice": nice_hits / (sour_hits + nice_hits + perfect_hits),
                             "perfect": perfect_hits / (sour_hits + nice_hits + perfect_hits)}
            sour = contact_rates["sour"]
            nice = contact_rates["nice"]
            perfect = contact_rates["perfect"]
            average = round((singles + doubles + triples + homeruns) / plate_appearances, 3)


        except ZeroDivisionError:
            continue
        from swing_type_func import swing_type

        swing_type(swing)
        user_dict[user] = (
        singles, doubles, triples, homeruns, rbi, plate_appearances, strikeouts, multi_out, outs, perfect_hits,
        sour_hits, nice_hits, extra_base_hits, contact_rates, sour, nice, perfect, average)
    except KeyError:
        continue


# sorted_user_list = sorted(user_dict.keys(), key=lambda x: user_dict[x][5], reverse=True)
#
# for user in sorted_user_list:
#     singles = user_dict[user][0]
#     doubles = user_dict[user][1]
#     triples = user_dict[user][2]
#     homeruns = user_dict[user][3]
#     rbi = user_dict[user][4]
#     plate_appearances = user_dict[user][5]
#     strikeouts = user_dict[user][6]
#     multi_out = user_dict[user][7]
#     outs = user_dict[user][8]
#     perfect_hits = user_dict[user][9]
#     nice_hits = user_dict[user][10]
#     sour_hits = user_dict[user][11]
#
#     if plate_appearances > 0:
#         print(user + ":", plate_appearances, "PA / ", singles, " / ", doubles, " / ", triples, " / ", homeruns)
