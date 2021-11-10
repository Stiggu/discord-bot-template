from discord.ext import commands
from cogs.message_parser import parse_message


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
        :return:
        """
        parse_message(message.content)


def setup(client):
    """
    Called by the main file, sets up the cog to be used
    :param client:
    :return:
    """
    client.add_cog(Listener(client))