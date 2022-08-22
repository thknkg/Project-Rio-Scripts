from collections import defaultdict

# take user input, including aliases and convert to character id number / "proper name" as stored in detailed_stats, etc.

# dict of character aliases and corresponding character ID
cCHAR_ALIASES = {
    'mario': 0,
    'mar': 0,
    'luigi': 1,
    'weegee': 1,
    'lu': 1,
    'dk': 2,
    'donkeykong': 2,
    'diddy': 3,
    'diddykong': 3,
    'peach': 4,
    'daisy': 5,
    'yoshi': 6,
    'yosh': 6,
    'babymario': 7,
    'bmario': 7,
    'bluigi': 8,
    'babyluigi': 8,
    'bowser': 9,
    'bow': 9,
    'wario': 10,
    'waluigi': 11,
    'walu': 11,
    'koopa(g)': 12,
    'gkoopa': 12,
    'greenkoopa': 12,
    'greenkoopatroopa': 12,
    'toad(r)': 13,
    'rtoad': 13,
    'toadred': 13,
    'redtoad': 13,
    'toad': 13,
    'boo': 14,
    'toadette': 15,
    'tdette': 15,
    'shyguy(r)': 16,
    'shyguyred': 16,
    'redshyguy': 16,
    'redguy': 16,
    'rsg': 16,
    'shyguy': 16,
    'birdo': 17,
    'monty': 18,
    'montymole': 18,
    'moonball': 18,
    'bowser jr': 19,
    'bj': 19,
    'bowserjunior': 19,
    'jr': 19,
    'paratroopa(r)': 20,
    'koopaparatroopared': 20,
    'redkoopaparatroopa': 20,
    'parared': 20,
    'redpara': 20,
    'rpara': 20,
    'ptred': 20,
    'redpt': 20,
    'pianta(b)': 21,
    'piantablue': 21,
    'bluepianta': 21,
    'blueblob': 21,
    'bb': 21,
    'pianta(r)': 22,
    'piantared': 22,
    'redpianta': 22,
    'pm': 22,
    'pianta(y)': 23,
    'piantayellow': 23,
    'yellowpianta': 23,
    'yellafella': 23,
    'yellowfellow': 23,
    'yf': 23,
    'noki(b)': 24,
    'nokiblue': 24,
    'bluenoki': 24,
    'boki': 24,
    'bnoki': 24,
    'bnoke': 24,
    'noki(r)': 25,
    'nokired': 25,
    'rednoki': 25,
    'gnoki': 26,
    'noki(g)': 26,
    'nokigreen': 26,
    'greennoki': 26,
    'mintnoki': 26,
    'gnoke': 26,
    'gnocchi': 26,
    'bro(h)': 27,
    'hammerbro': 27,
    'hammer': 27,
    'h!bro': 27,
    'hbro': 27,
    'toadsworth': 28,
    'tw': 28,
    'peterose': 28,
    'oldman': 28,
    'toad(b)': 29,
    'toadblue': 29,
    'bluetoad': 29,
    'btoad': 29,
    'teardrop': 29,
    'toad(y)': 30,
    'toadyellow': 30,
    'yellowtoad': 30,
    'peetoad': 30,
    'cornpop': 30,
    'toad(g)': 31,
    'toadgreen': 31,
    'greentoad': 31,
    'gtoad': 31,
    'toad(p)': 32,
    'toadpurple': 32,
    'purpletoad': 32,
    'leantoad': 32,
    'ptoad': 32,
    'magikoopa(b)': 33,
    'magikoopablue': 33,
    'bluemagikoopa': 33,
    'magblue': 33,
    'bluemag': 33,
    'mageblue': 33,
    'bluemage': 33,
    'bmage': 33,
    'bmag': 33,
    'magikoopa(r)': 34,
    'magikoopared': 34,
    'redmagikoopa': 34,
    'magred': 34,
    'redmag': 34,
    'magered': 34,
    'redmage': 34,
    'rmag': 34,
    'rmage': 34,
    'magikoopa(g)': 35,
    'magikoopagreen': 35,
    'greenmagikoopa': 35,
    'maggreen': 35,
    'greenmag': 35,
    'magegreen': 35,
    'greenmage': 35,
    'gmag': 35,
    'gmage': 35,
    'magikoopa(y)': 36,
    'magikoopayellow': 36,
    'yellowmagikoopa': 36,
    'magyellow': 36,
    'yellowmag': 36,
    'mageyellow': 36,
    'yellowmage': 36,
    'pisswizard': 36,
    'pisswizz': 36,
    'pizzwizz': 36,
    'weezard': 36,
    'ymag': 36,
    'kingboo': 37,
    'kboo': 37,
    'kb': 37,
    'peteypirahana': 38,
    'petey': 38,
    'peaty': 38,
    'peety': 38,
    'peter': 38,
    'dixiekong': 39,
    'dixie': 39,
    'goomba': 40,
    'goombo': 40,
    'dingus': 40,
    'paragoomba': 41,
    'wingombo': 41,
    'parag': 41,
    'pg': 41,
    'koopa(r)': 42,
    'koopa': 42,
    'koopatroopa': 42,
    'redkoopa': 42,
    'redkoopatroopa': 42,
    'koopared': 42,
    'koopatroopared': 42,
    'rkoopa': 42,
    'rafa': 42,
    'rafael': 42,
    'ron': 42,
    'ronald': 42,
    'paratroopa(g)': 43,
    'koopaparatroopagreen': 43,
    'greenkoopaparatroopa': 43,
    'paragreen': 43,
    'greenpara': 43,
    'ptgreen': 43,
    'greenpt': 43,
    'para': 43,
    'parat': 43,
    'pt': 43,
    'gpara': 43,
    'shyguy(b)': 44,
    'shyguyblue': 44,
    'blueshyguy': 44,
    'blueguy': 44,
    'bsg': 44,
    'bshyguy':44,
    'shyguy(y)': 45,
    'shyguyyellow': 45,
    'blueshyyellow': 45,
    'yellowguy': 45,
    'ysg': 45,
    'yshyguy':45,
    'shyguy(g)': 47,
    'shyguygreen': 47,
    'greenshyguy': 47,
    'greenguy': 47,
    'gsg': 47,
    'gshyguy':47,
    'shyguy(bk)': 48,
    'shyguyblack': 48,
    'blackshyguy': 48,
    'blackguy': 48,
    'blsg': 48,
    'blshyguy':48,
    'drybones(gy)': 49,
    'drybones': 49,
    'bones': 49,
    'drybonesgray': 49,
    'drybonesgrey': 49,
    'greydrybones': 49,
    'graydrybones': 49,
    'bonesgray': 49,
    'bonesgrey': 49,
    'greybones': 49,
    'graybones': 49,
    'barebones': 49,
    'drybones(g)': 50,
    'drybonesgreen': 50,
    'greendrybones': 50,
    'bonesgreen': 50,
    'greenbones': 50,
    'gbones': 50,
    'drybones(r)': 51,
    'drybonesred': 51,
    'reddrybones': 51,
    'bonesred': 51,
    'redbones': 51,
    'rbones': 51,
    'drybones(b)': 52,
    'drybonesblue': 52,
    'bluedrybones': 52,
    'bonesblue': 52,
    'bluebones': 52,
    'bbones': 52,
    'bro(f)': 53,
    'fire': 53,
    'firebro': 53,
    'f!bro': 53,
    'fbro': 53,
    'bro(b)': 54,
    'boomerbro': 54,
    'boomer': 54,
    'b!bro': 54,
    'bbro': 54}

# converted to a list so that all 54's were together in a list, etc.
alias_dict = defaultdict(list)

# inverted it so that key is character id and value is list of nicknames
for char, num in cCHAR_ALIASES.items():
    alias_dict[num].append(char)

# input given by user
user_char_select = input()

# function to convert input to lowercase, check the dict, and give the corresponding char/character ID
def char_alias():
    user_char_select.lower().replace(" ", "")
    for id_num, nickname in alias_dict.items():
     if user_char_select in nickname:
        global character_id
        character_id = id_num
        global character
        character = nickname



        # dict with character ID as keys and actual Rio names as values
        rio_key_dict = {
                0: "Mario",
                1: "Luigi",
                2: "DK",
                3: "Diddy",
                4: "Peach",
                5: "Daisy",
                6: "Yoshi",
                7: "Baby Mario",
                8: "Baby Luigi",
                9: "Bowser",
                10: "Wario",
                11: "Waluigi",
                12: "Koopa(G)",
                13: "Toad(R)",
                14: "Boo",
                15: "Toadette",
                16: "Shy Guy(R)",
                17: "Birdo",
                18: "Monty",
                19: "Bowser Jr",
                20: "Paratroopa(R)",
                21: "Pianta(B)",
                22: "Pianta(R)",
                23: "Pianta(Y)",
                24: "Noki(B)",
                25: "Noki(R)",
                26: "Noki(G)",
                27: "Bro(H)",
                28: "Toadsworth",
                29: "Toad(B)",
                30: "Toad(Y)",
                31: "Toad(G)",
                32: "Toad(P)",
                33: "Magikoopa(B)",
                34: "Magikoopa(R)",
                35: "Magikoopa(G)",
                36: "Magikoopa(Y)",
                37: "King Boo",
                38: "Petey",
                39: "Dixie",
                40: "Goomba",
                41: "Paragoomba",
                42: "Koopa(R)",
                43: "Paratroopa(G)",
                44: "Shy Guy(B)",
                45: "Shy Guy(Y)",
                46: "Shy Guy(G)",
                47: "Shy Guy(Bk)",
                48: "Dry Bones(Gy)",
                49: "Dry Bones(G)",
                50: "Dry Bones(R)",
                51: "Dry Bones(B)",
                52: "Bro(F)",
                53: "Bro(B)",
                None: "None"
        }
        # convert the results of the function via the second dict
        final_result = rio_key_dict[character_id]

        # output the correct form needed to access the key correctly
        return final_result, character_id

# call the function (if stopped at this point, can also just give the char_id for other endpoints)
user_input_result = char_alias()
dict_name = user_input_result[0]
id_num = user_input_result[1]

# print(dict_name, id_num)

