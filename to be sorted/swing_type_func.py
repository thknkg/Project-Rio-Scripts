from by_swing_type import total_char_response, user, char, user_dict, stats
from make_percentage import percentage, add_percent_sign
def swing_type(type):
    stats = total_char_response["Stats"][user][char]["Batting"][type]
    if stats["plate_appearances"] > 0:

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

        extra_base_hits = round((doubles+triples+homeruns) / (singles+doubles+triples+homeruns)*100, 1)
        contact_rates = {"sour": sour_hits / (sour_hits + nice_hits + perfect_hits), "nice": nice_hits / (sour_hits + nice_hits + perfect_hits), "perfect": perfect_hits / (sour_hits + nice_hits + perfect_hits)}
        sour = contact_rates["sour"]
        nice = contact_rates["nice"]
        perfect = contact_rates["perfect"]
        average = round((singles + doubles + triples + homeruns) / plate_appearances, 3)

sorted_user_list = sorted(user_dict.keys(), key=lambda x: user_dict[x][12], reverse=True)

for user in sorted_user_list:
    singles = user_dict[user][0]
    doubles = user_dict[user][1]
    triples = user_dict[user][2]
    homeruns = user_dict[user][3]
    rbi = user_dict[user][4]
    plate_appearances = user_dict[user][5]
    strikeouts = user_dict[user][6]
    multi_out = user_dict[user][7]
    outs = user_dict[user][8]
    perfect_hits = user_dict[user][9]
    nice_hits = user_dict[user][10]
    sour_hits = user_dict[user][11]
    extra_base_hits = user_dict[user][12]
    contact_rates = user_dict[user][13]
    sour = user_dict[user][14]
    nice = user_dict[user][15]
    perfect = user_dict[user][16]
    average = user_dict[user][17]

    if plate_appearances >= 10:
        # print(user, "/", average)
        # print(user + ":", plate_appearances, "PA / ", singles, " / ", doubles, " / ", triples, " / ", homeruns, " / ",  str(extra_base_hits) + "% extra base hits")
        print(str(extra_base_hits) + "% extra base hits / ", rbi, "RBI")
        print(user, add_percent_sign(percentage(contact_rates["sour"])) + " sour / ", add_percent_sign(percentage(contact_rates["nice"])) + " nice / ", add_percent_sign(percentage(contact_rates["perfect"])) + " perfect\n")
