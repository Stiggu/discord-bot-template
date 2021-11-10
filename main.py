from discord.ext import commands
from cogs.secret_variables import token


def load_cogs(client):
    """
    Used to load the cogs/extensions of the bot
    :param client: discord client / bot itself
    :return:
    """
    client.load_extension("cogs.message_listener")


def run_bot():
    """
    Sets certain options for the bot, loads the cogs then starts it
    :return:
    """
    client = commands.Bot(command_prefix="!", case_insensitive=True)

    load_cogs(client)

    client.run(token)


if __name__ == '__main__':
    run_bot()
