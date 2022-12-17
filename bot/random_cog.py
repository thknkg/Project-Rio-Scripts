from io import BytesIO

import discord
from discord.ext import commands

from randomizers.RandomFunctions import *
from helpers.ImageBuilder import *
from helpers.TeamSort import *

class RandomizeCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="random",
                 help="Random Baseball functions. Current commands [Character, Stadium, Teams, Power Teams")
    async def _random(ctx, command, qualifier=""):
        command = command.lower()
        qualifier = qualifier.lower()
        if command == "character" or command == "chara" or command == "char":
            await ctx.send(rfRandomCharacter())
        elif command == "stadium":
            await ctx.send(rfRandomStadium())
        elif command == "teams":

            if not qualifier or qualifier == "":
                team_list = rfRandomTeamsWithoutDupes()
                title = "**Random Teams** — without dupes, random variants"
            elif "dupes" in qualifier:
                team_list = rfRandomTeamsWithDupes()
                title = "**Random Teams** — with dupes"
            elif "balanced" in qualifier:
                team_list = rfRandomBalancedTeams()
                title = "**Random Balanced Teams** — with dupes, balanced by 5 broad tiers"
            elif "power" in qualifier:
                team_list = rfRandomPowerTeams()
                title = "**Random Power Teams** — top 24 characters with dupes and distributed pitching"

            captain_list = [team_list[0][0], team_list[1][0]]
            team_list = sortTeamsByTier(team_list)

            teams_image = buildTeamImageHighlightCaptain(team_list, captain_list)

            with BytesIO() as image_binary:
                teams_image.save(image_binary, 'PNG')
                image_binary.seek(0)
                await ctx.send(title, file=discord.File(fp=image_binary, filename='image.png'))

        else:
            await ctx.send("Alas poor random command; I do not know thee well.")

    # END _random

    @commands.command(name="coin", help="Toss a coin to your witcher")
    async def _coin(ctx):
        await ctx.send(rfFlipCoin())

    # END _coin

    # TODO: COGS would be cool here; wouldn't it be cool to be able to call this with a 'D4', 'D6', 'D8', 'D10', 'D12', 'D20'
    @commands.command(name="roll", help="Roll a N sided die, where n is the parameter")
    async def _roll(ctx, die):
        try:
            number = int(die)
        except ValueError:
            await ctx.send("That isn't a die")
            return

        if number > 2:
            await ctx.send(rfRollDice(number))
        else:
            await ctx.send("I can't roll that here")

    # END _roll

    @commands.command(name="pick", help="Pick one item from a list of inputs")
    async def _pick(ctx, *arg):
        if len(arg) > 0:
            await ctx.send(rfPickOne(arg))
        else:
            await ctx.send("Please supply more options than that")

    # END _pick

    @commands.command(name="pickmany", help="When you need to pick N items from a list")
    async def _pickmany(ctx, choices, *arg):
        try:
            number = int(choices)
        except ValueError:
            await ctx.send("Give me a number of choices to make, gosh")
            return

        if len(arg) > 0 and number <= len(arg):
            await ctx.send(rfPickMany(number, arg))
        else:
            await ctx.send("I don't think you know what you're asking")

    # END _pickmany

    @commands.command(name="shuffle", help="Shuffle the order of a list")
    async def _shuffle(ctx, *arg):
        if len(arg) > 1:
            await ctx.send(rfShuffle(arg))
        else:
            await ctx.send("I don't feel like shuffling those")
    # END _shuffle

async def setup(client):
    await client.add_cog(RandomizeCommands(client))

