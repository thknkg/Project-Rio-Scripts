from random import shuffle, randint, choice, sample
from randomizers.RandomBaseball import randomTeamsWithoutDupes, randomTeamsWtihDupes, randomPowerTeams, randomBalancedTeams
from randomizers.RandomEnums import Stadium, Char

#Defines the random functions for the bot

# Flip a coin return heads or tails
def rfFlipCoin():
    if randint(0, 1) == 0:
        return "Heads"
    return "Tails"

# Roll a dice with DIE number of sides
def rfRollDice(die):
    if die > 1:
        return randint(1, die)
    return 1

# Pick One from a set of arguments
def rfPickOne(args):
    return choice(args)

# Pick N from a set of arguments. Picks all if N is equal too or greater than the number of arguments
def rfPickMany(choices, args):
    return sample(args, choices)

# Shuffle a set of arguments. We convert to a list because *args is a TUPLE and therefore is immutable
def rfShuffle(args):
    list = []
    for arg in args:
        list.append(arg)
    shuffle(list)
    return list

def rfRandomCharacter():
    characters = []
    for char in Char:
        characters.append(char.value)
    shuffle(characters)
    return characters.pop()

def rfRandomStadium():
    stadiums = []
    for stadium in Stadium:
        stadiums.append(stadium.value)
    shuffle(stadiums)
    return stadiums.pop()

def rfRandomMode():
    return

def rfRandomTeamsWithoutDupes():
    return randomTeamsWithoutDupes()

def rfRandomTeamsWithDupes():
    return randomTeamsWtihDupes()

def rfRandomBalancedTeams():
    return randomBalancedTeams()

def rfRandomPowerTeams():
    return randomPowerTeams()
