import random


def roll_dice(number: int, sides: int) -> list:
    """
    Rolls a x amount of dices with y number of sides
    :param number: int
    :param sides: int
    :return: int array with the rolls
    """

    return [random.randint(0, sides) for x in range(number)]


def parse_message(message: str) -> list:
    """
    Will parse the message into something useful
    :param str message: Message from an user
    :return: Returns an array with parsed data
    """

    message_array_with_dice_data = message.split(':')[:2]

    dices = "".join(filter(str.isdigit, message_array_with_dice_data[0]))
    sides = "".join(filter(str.isdigit, message_array_with_dice_data[1]))

    return [dices, sides]
