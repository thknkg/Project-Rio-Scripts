import requests

print("Enter name of character (blank for all stats):")
char = input()
print("Enter '0' for stars-off data; '1' for stars-on")
stars = int(input())
print("Enter '0' for all data, '1' for ranked only")
ranked = int(input())

url = "https://projectrio-api-1.api.projectrio.app/detailed_stats/?exclude_pitching=1&exclude_fielding=1&exclude_misc=1"
if stars == 0:
    url += "&tag=Normal"
elif stars == 1:
    url += "&tag=Superstar"
if ranked == 1:
    url += "&tag=Ranked"

if char != "":
    url += "&by_char=1"

total_response = requests.get(url).json()
print(url)

url += "&by_user=1"

user_response = requests.get(url).json()

user_dict = {}

overall = {}
if char == "":
    overall = total_response["Stats"]["Batting"]["Star"]
else:
    overall = total_response["Stats"][char]["Batting"]["Star"]
overall_obp = (overall["summary_hits"] + overall["summary_walks_hbp"] + overall["summary_walks_bb"]) / overall["plate_appearances"]
overall_slg = (overall["summary_singles"] + (overall["summary_doubles"] * 2) + (overall["summary_triples"] * 3) + (overall["summary_homeruns"] * 4)) / overall["summary_at_bats"]

for user in user_response["Stats"]:
    # todo
    stats = {}
    if char == "":
        stats = user_response["Stats"][user]["Batting"]
    elif char in user_response["Stats"][user]:
        stats = user_response["Stats"][user][char]["Batting"]
    else:
        continue
    if "plate_appearances" in stats and "summary_at_bats" in stats:
        if stats["plate_appearances"] > 0:
            avg = stats["singles"] + stats["triples"] + stats["doubles"] + stats["homeruns"]  / stats["plate_appearances"]
            obp = (stats["summary_hits"] + stats["summary_walks_hbp"] + stats["summary_walks_bb"]) / stats["plate_appearances"]
            slg = (stats["summary_singles"] + (stats["summary_doubles"] * 2) + (stats["summary_triples"] * 3) + (stats["summary_homeruns"] * 4)) / stats["summary_at_bats"]
            ops = obp + slg
            pa = stats["plate_appearances"]
            ops_plus = ((obp / overall_obp) + (slg / overall_slg) - 1) * 100
            user_dict[user] = (pa, avg, obp, slg, ops, ops_plus)

sorted_user_list = sorted(user_dict.keys(), key=lambda x: user_dict[x][5], reverse=True)

print("AVG / OBP / SLG / OPS")

for user in sorted_user_list:
    pa = user_dict[user][0]
    avg = user_dict[user][1]
    obp = user_dict[user][2]
    slg = user_dict[user][3]
    ops = user_dict[user][4]
    ops_plus = user_dict[user][5]
    if pa > 0:
        print(user + " (" + str(pa) + " PA): " + "{:.3f}".format(avg) + " / " + "{:.3f}".format(obp) + " / " + "{:.3f}".format(slg) + " / " + "{:.3f}".format(ops) + ", " + str(round(ops_plus)) + " cOPS+")
