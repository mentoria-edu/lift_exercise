from random import randint
from time import sleep

from src.chance import happens_by_chance
from src.constant import FLOOR_AMOUNT
from src.logger_config import info
from src.passenger import register_floor_passenger


def call_elevator(
        floor_passenger: dict
) -> dict:

    floor_amount = FLOOR_AMOUNT
    call_chance = 0.3
    new_floor_passenger = {}
    random_floor = randint(0, floor_amount)

    if happens_by_chance(
        chance_modifier=call_chance
    ) and not floor_passenger.get(random_floor):

        called_floor = random_floor

        new_floor_passenger = register_floor_passenger(
            called_floor=called_floor
        )

        info(f'Floor no. {called_floor} has been called.')

        sleep(1)

    return new_floor_passenger
