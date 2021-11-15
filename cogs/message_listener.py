import discord.errors
from discord.ext import commands
from cogs.message_parser import parse_message, roll_dice


class Listener(commands.Cog):
    def __init__(self, client):
        """
        Constructor - Sets up variables for later use
        :param client:
        """
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        """
        Listen to every message that is sent on the server
        :param message: Contains Data (Check the API reference, this message has certain limitations)
        """

        if ":dr" in message.content:
            number_of_dices, sides = parse_message(message.content)

            try:
                number_of_dices = int(number_of_dices)
                sides = int(sides)
            except ValueError:
                return await message.channel.send("Invalid query!")

            rolls = roll_dice(number_of_dices, sides)
            try:
                await message.channel.send(rolls)
            except discord.errors.HTTPException:
                await message.channel.send("You used to many dices, are you crazy?")


def setup(client):
    """
    Called by the main file, sets up the cog to be used
    :param client:
    """
    client.add_cog(Listener(client))