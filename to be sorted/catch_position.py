from glob import glob
import json
from math import sqrt


def PosDistance(event, position, x, y , z):
    for event in file["Events"]:
        try:
            if event["Pitch"]["Contact"]["First Fielder"]["Fielder Position"] == position and \
                    event["Runner Batter"]["Out Type"] == "Caught" and character["Superstar"] == 0:
                ball_pos_x = (x) - event["Pitch"]["Contact"]["Ball Landing Position - X"]

                ball_pos_y = (y) - event["Pitch"]["Contact"]["Ball Landing Position - Y"]

                ball_pos_z = (z) - event["Pitch"]["Contact"]["Ball Landing Position - Z"]

                ball_sum = round(sqrt((ball_pos_x ** 2) + (ball_pos_z ** 2)), 3)

            def distance(char, char_list):
                if event["Pitch"]["Contact"]["First Fielder"]["Fielder Character"] == char:
                    char_list.append(ball_sum)

            for char in character_dict:
                distance(char, character_dict[char]["Events"]["Distance"])
        except KeyError:
            pass
