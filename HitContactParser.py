import json
from glob import glob

for f_name in glob('*.json'):
    if f_name in glob('decoded.*'):
        with open(f_name) as json_file:
            try:
                stat_file = json.load(json_file)

                # print(type(stat_file))
                for data in stat_file["Events"][:]:
                    # print(type(data))
                    try:
                        pitch = data["Pitch"]
                        contact = pitch.get("Contact", "No contact")
                        if stat_file["Away Player"] == "MORI" and pitch["Pitcher Team Id"] == 0:
                            if pitch.get("Pitch Result") == "Strike-swing" or pitch.get(
                                    "Pitch Result") == "Strike-looking" or pitch.get("Pitch Result") == "Ball":
                                try:
                                    contact = pitch.get("Contact", "No contact")
                                    print(contact["Contact Result - Primary"])
                                except KeyError:
                                    continue
                            """if pitch.get("Contact Result - Primary", "No result") != "Foul":
                                                                # print(type(data))
                                                                pitch = data["Pitch"]
                                                                contact = pitch.get("Contact", "No contact")
                                                                # print(type(contact))
                                                                if type(contact) == dict and contact.get("Contact Result - Primary") != "Foul":
                                                                        #hit_type = print(contact.get("Type of Contact") + ",", contact.get("Contact Result - Primary") + ",", contact.get("Contact Result - Secondary"), ",", pitch.get("Pitch Result"))
                                                                        if pitch.get("Pitch Result") != "Contact":
                                                                                print(contact.get("Contact Result - Primary"))
                                                                else:
                                                                        print("Foul")
                                                                        # continue"""
                        elif stat_file["Home Player"] == "MORI" and pitch["Pitcher Team Id"] == 1:
                            if pitch.get("Pitch Result") == "Strike-swing" or pitch.get(
                                    "Pitch Result") == "Strike-looking" or pitch.get("Pitch Result") == "Ball":
                                try:
                                    contact = pitch.get("Contact", "No contact")
                                    print(contact)
                                except KeyError:
                                    continue
                            """if pitch.get("Contact Result - Primary", "No result") != "Foul":
                                                                # print(type(data))
                                                                pitch = data["Pitch"]
                                                                contact = pitch.get("Contact", "No contact")
                                                                # print(type(contact))
                                                                if type(contact) == dict and contact.get("Contact Result - Primary") != "Foul":
                                                                        #hit_type = print(contact.get("Type of Contact") + ",", contact.get("Contact Result - Primary") + ",", contact.get("Contact Result - Secondary"), ",", pitch.get("Pitch Result"))
                                                                        if pitch.get("Pitch Result") != "Contact":
                                                                                print(contact.get("Contact Result - Primary"))
                                                                else:
                                                                        print("Foul")
                                                                        # continue"""
                    except KeyError:
                        continue
            except json.decoder.JSONDecodeError:
                continue
