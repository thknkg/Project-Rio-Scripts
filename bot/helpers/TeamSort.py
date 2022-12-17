from randomizers.RandomEnums import Char

ranked_character_dict = {
    "Mario": 13,
    "Luigi": 16,
    "DK": 3,
    "Diddy": 17,
    "Peach": 26,
    "Daisy": 23,
    "Yoshi": 5,
    "Baby Mario": 37,
    "Baby Luigi": 37,
    "Bowser": 1,
    "Wario": 14,
    "Waluigi": 11,
    "Koopa(G)": 31,
    "Toad(R)": 29,
    "Boo": 7,
    "Toadette": 20,
    "Shy Guy(R)": 27,
    "Birdo": 6,
    "Monty": 32,
    "Bowser Jr": 21,
    "Paratroopa(R)": 33,
    "Pianta(B)": 24,
    "Pianta(R)": 15,
    "Pianta(Y)": 24,
    "Noki(B)": 25,
    "Noki(R)": 25,
    "Noki(G)": 18,
    "Bro(H)": 4,
    "Toadsworth": 12,
    "Toad(B)": 36,
    "Toad(Y)": 36,
    "Toad(G)": 36,
    "Toad(P)": 36,
    "Magikoopa(B)": 10,
    "Magikoopa(R)": 10,
    "Magikoopa(G)": 10,
    "Magikoopa(Y)": 10,
    "King Boo": 8,
    "Petey": 2,
    "Dixie": 17,
    "Goomba": 38,
    "Paragoomba": 38,
    "Koopa(R)": 34,
    "Paratroopa(G)": 19,
    "Shy Guy(B)": 30,
    "Shy Guy(Y)": 30,
    "Shy Guy(G)": 27,
    "Shy Guy(Bk)": 30,
    "Dry Bones(Gy)": 35,
    "Dry Bones(G)": 22,
    "Dry Bones(R)": 28,
    "Dry Bones(B)": 35,
    "Bro(F)": 9,
    "Bro(B)": 4
}

def getCharacterRank(char):
    return ranked_character_dict[char.value]
#END getCharacterRank

def sortTeamByTier(team):
    captain = team.pop(0)
    team.sort(key=getCharacterRank)
    team.insert(0, captain)
    return team
#END Sort Team By Tier

def sortTeamsByTierExcludeCaptain(teams):
    for team in teams:
        captain = team.pop(0)
        team.sort(key=getCharacterRank)
        team.insert(0, captain)
    return teams
#END Sort Teams By Tier Exclude Captain

def sortTeamsByTier(teams):
    for team in teams:
        team.sort(key=getCharacterRank)
    return teams
#END Sort Teams By Tier Exclude Captain