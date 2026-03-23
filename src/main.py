from time import sleep

from src.movement import stand_by, move
from src.priority import check_priority
from src.call import call_elevator
from src.logger_config import debug, info, error, config_logger


def exec_lift() -> None:

    passenger_aboard = 0
    current_floor = 0
    destination = []
    floor_passenger = {}
    floor_queue = []

    while True:

        debug(
            '(invariant check - stop_lift exit) '
            f'passenger_aboard={passenger_aboard}, '
            f'destinations={destination}, '
            f'len(destination)={len(destination)}'
        )

        if len(destination) != passenger_aboard:

            error(
                '(func exec_lift) '
                'destinations amount does not match '
                'with passengers aboard: '
                f'destinations: {destination}, '
                f'passengers aboard: {passenger_aboard}'
            )

        while not len(floor_passenger) and not passenger_aboard:

            stand_by(current_floor=current_floor)
            sleep(2)

            floor_passenger.update(call_elevator(
                floor_passenger=floor_passenger
            ))
            floors = floor_passenger.keys()
            floor_queue.extend(floors)


        new_priority = check_priority(
            passenger_aboard=passenger_aboard,
            floor_queue=floor_queue,
            destination=destination,
        )

        floor_queue = new_priority['sorted_queue']
        destination = new_priority['sorted_destination']

        info(f'Passengers aboard: {passenger_aboard}, '
            'Floors called (floor:passenger amount): '
            f'{floor_passenger}, '
            f'Passengers will unboard at: {destination}'
        )

        debug(
            '(func exec_lift) '
            'params after check_priority: '
            f'current_floor = {current_floor}, '
            f'passenger_aboard = {passenger_aboard}, '
            f'floor_passenger = {floor_passenger}, '
            f'floor_queue = {floor_queue}, '
            f'destination = {destination}'
        )

        updated_params = move(
            current_floor=current_floor,
            passenger_aboard=passenger_aboard,
            floor_queue=floor_queue,
            destination=destination,
            floor_passenger=floor_passenger,
        )

        debug(
            '(func exec_lift) '
            'updated_params: '
            f'{updated_params}'
        )

        current_floor = updated_params['updated_current_floor']
        passenger_aboard = updated_params['updated_passenger_aboard']
        floor_passenger = updated_params['updated_floor_passenger']
        destination = updated_params['updated_destination']
        floor_queue = updated_params['updated_floor_queue']

        debug(
            '(func exec_lift) '
            'params at end of cycle: '
            f'current_floor = {current_floor}, '
            f'passenger_aboard = {passenger_aboard}, '
            f'floor_passenger = {floor_passenger}, '
            f'floor_queue = {floor_queue}, '
            f'destination = {destination}'
        )

        sleep(1)


config_logger()
exec_lift()
