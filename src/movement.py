from time import sleep

from src.passenger import unboard_passenger, board_passenger
from src.logger_config import info, debug
from src.call import call_elevator
from src.priority import check_priority


def stand_by(current_floor: int) -> None:

    info(
        'No floor called, '
        'the lift is waiting at '
        f'floor no. {current_floor}.'
        if current_floor != 0
        else
        'No floor called, '
        'the lift is waiting at '
        'ground floor.'
    )

    return


def stop_lift(
        current_floor: int,
        floor_passenger: dict,
        passenger_aboard: int,
        floor_queue: list,
        destination: list
) -> dict:
    
    debug(
        '(func stop_lift - entry) '
        f'current_floor={current_floor}, '
        f'passenger_aboard={passenger_aboard}, '
        f'destination={destination}, '
        f'floor_queue={floor_queue}, '
        f'floor_passenger={floor_passenger}'
    )

    info(f'Lift has stopped by floor {current_floor}')
    info('Lift door opened.')
    sleep(2)

    if destination.count(current_floor):

        updated_unboard_passengers = unboard_passenger(
            passenger_aboard=passenger_aboard,
            current_floor=current_floor,
            destination=destination
        )

        new_passenger_aboard = updated_unboard_passengers[
            'updated_passenger_aboard'
        ]
        new_destination = updated_unboard_passengers[
            'updated_destination'
        ]

        destination = new_destination

        passenger_aboard = new_passenger_aboard

        debug(
            '(func stop_lift - AFTER UNBOARD) '
            f'old_passenger_aboard={passenger_aboard}, '
            f'new_passenger_aboard={new_passenger_aboard}, '
            f'old_destination={destination}, '
            f'new_destination={new_destination}'
        )

    if floor_passenger.get(current_floor):

        updated_board_passenger = board_passenger(
            current_floor=current_floor,
            floor_passenger=floor_passenger,
            passenger_aboard=passenger_aboard,
            floor_queue=floor_queue,
            destination=destination
        )

        floor_passenger = updated_board_passenger[
            'updated_floor_passenger'
        ]
        new_passenger_aboard = updated_board_passenger[
            'updated_passenger_aboard'
        ]
        new_destination = updated_board_passenger[
            'updated_destination'
        ]
        floor_queue = updated_board_passenger[
            'updated_floor_queue'
        ]

        debug(
            '(func stop_lift - AFTER BOARD) '
            f'old_passenger_aboard={passenger_aboard}, '
            f'new_passenger_aboard={new_passenger_aboard}, '
            f'old_destination={destination}, '
            f'new_destination={new_destination}, '
            f'floor_queue={floor_queue}'
	    )

    info('Lift door closed.')
    sleep(2)

    updated_params = {
        'updated_floor_passenger':floor_passenger,
        'updated_passenger_aboard':new_passenger_aboard,
        'updated_destination':new_destination,
        'updated_floor_queue':floor_queue
    }

    return updated_params


def set_path(
        passenger_aboard: int,
        floor_queue: list,
        destination: list,
) -> list:

    path = []

    if passenger_aboard and destination:

        path = destination

        debug(
            '(func set_path) '
            'path will be destination'
        )

    elif not passenger_aboard and floor_queue:

        path = floor_queue

        debug(
            '(func set_path) '
            'path will be floor_queue'
        )

    else:

        debug(
            '(func move) '
            'following no path, staying still'
        )

    debug(
    '(func set_path) '
    f'passenger_aboard={passenger_aboard}, '
    f'floor_queue={floor_queue}, '
    f'destination={destination}'
)
    
    debug(f'(func set_path) resolved path={path}')

    return path


def move(
        current_floor: int,
        passenger_aboard: int,
        floor_queue: list,
        destination: list,
        floor_passenger: dict
) -> dict:

    path = set_path(
        passenger_aboard=passenger_aboard,
        floor_queue=floor_queue,
        destination=destination
    )

    if not len(path):

        updated_params = {
            'updated_current_floor': current_floor,
            'updated_passenger_aboard': passenger_aboard,
            'updated_floor_passenger': floor_passenger,
            'updated_destination': destination,
            'updated_floor_queue': floor_queue
        }

        return updated_params

    debug(f'this is the path: {path}')

    debug(
    '(path access) '
    f'path={path}, '
    f'current_floor={current_floor}'
)

    if path and path[0] > current_floor:

        debug('I\'m going up')

        debug(
            '(path access) '
            f'path={path}, '
            f'current_floor={current_floor}'
        )

        while path and current_floor < path[0]:

            new_floor_passenger = call_elevator(
                floor_passenger=floor_passenger
            )
            floors = new_floor_passenger.keys()
            floor_queue.extend(floors)
            floor_passenger.update(new_floor_passenger)
            
            updated_priority = check_priority(
                passenger_aboard=passenger_aboard,
                floor_queue=floor_queue,
                destination=destination
            )

            floor_queue = updated_priority['sorted_queue']
            destination = updated_priority['sorted_destination']

            new_path = set_path(
                passenger_aboard=passenger_aboard,
                floor_queue=floor_queue,
                destination=destination
            )

            if not new_path:
                break

            current_floor += 1

            info(f'The lift is going up: Floor {current_floor}')
            debug(f'current floor = {current_floor}')
            sleep(1)

            if new_path.count(current_floor) and max(new_path) == current_floor:
                
                updated_params_while_up = stop_lift(
                    current_floor=current_floor,
                    floor_passenger=floor_passenger,
                    passenger_aboard=passenger_aboard,
                    floor_queue=floor_queue,
                    destination=destination
                )
            
                floor_passenger = updated_params_while_up[
                    'updated_floor_passenger'
                ]
                passenger_aboard = updated_params_while_up[
                    'updated_passenger_aboard'
                ]
                destination = updated_params_while_up[
                    'updated_destination'
                ]
                floor_queue = updated_params_while_up[
                    'updated_floor_queue'
                ]
                new_path = set_path(
                passenger_aboard=passenger_aboard,
                floor_queue=floor_queue,
                destination=destination
                )

        path = new_path

    debug(
        '(func move) '
        f'path = {path}, floor_queue = {floor_queue}'
    )

    path = set_path(
        passenger_aboard=passenger_aboard,
        floor_queue=floor_queue,
        destination=destination
    )

    debug(
        '(path access) '
        f'path={path}, '
        f'current_floor={current_floor}'
    )

    if path and path[0] < current_floor:

        debug('I\'m going down')

        info(f'The lift is starting to move down: Floor {current_floor}')
        sleep(1)

        debug(
            '(path access) '
            f'path={path}, '
            f'current_floor={current_floor}'
        )

        while path and current_floor > path[0]:

            new_floor_passenger = call_elevator(
                floor_passenger=floor_passenger
            )
            floors = new_floor_passenger.keys()
            floor_queue.extend(floors)
            floor_passenger.update(new_floor_passenger)

            updated_priority = check_priority(
                passenger_aboard=passenger_aboard,
                floor_queue=floor_queue,
                destination=destination
            )

            floor_queue = updated_priority['sorted_queue']
            destination = updated_priority['sorted_destination']

            new_path = set_path(
                passenger_aboard=passenger_aboard,
                floor_queue=floor_queue,
                destination=destination
            )

            if not new_path:
                break

            current_floor -= 1

            info(f'The lift is going down: Floor {current_floor}')
            debug(f'current floor = {current_floor}')
            sleep(1)

            if (
                floor_queue.count(current_floor)
                or destination.count(current_floor)
            ):
                
                updated_params_while_down = stop_lift(
                    current_floor=current_floor,
                    floor_passenger=floor_passenger,
                    passenger_aboard=passenger_aboard,
                    floor_queue=floor_queue,
                    destination=destination
                )
            
                floor_passenger = updated_params_while_down[
                    'updated_floor_passenger'
                ]
                passenger_aboard = updated_params_while_down[
                    'updated_passenger_aboard'
                ]
                destination = updated_params_while_down[
                    'updated_destination'
                ]
                floor_queue = updated_params_while_down[
                    'updated_floor_queue'
                ]
                new_path = set_path(
                passenger_aboard=passenger_aboard,
                floor_queue=floor_queue,
                destination=destination
                )

        path = new_path

    debug(
        '(path access) '
        f'path={path}, '
        f'current_floor={current_floor}'
    )

    if path and path[0] == current_floor:

        debug('I\'m stopping at current floor')

        updated_params = stop_lift(
        current_floor=current_floor,
        floor_passenger=floor_passenger,
        passenger_aboard=passenger_aboard,
        floor_queue=floor_queue,
        destination=destination
        )

        floor_passenger = updated_params[
            'updated_floor_passenger'
        ]
        passenger_aboard = updated_params[
            'updated_passenger_aboard'
        ]
        destination = updated_params[
            'updated_destination'
        ]
        floor_queue = updated_params[
            'updated_floor_queue'
        ]

    path = set_path(
        passenger_aboard=passenger_aboard,
        floor_queue=floor_queue,
        destination=destination
    )

    updated_params = {
        'updated_current_floor': current_floor,
        'updated_passenger_aboard':passenger_aboard,
        'updated_floor_queue':floor_queue,
        'updated_destination':destination,
        'updated_floor_passenger':floor_passenger
    }

    debug(
        '(func move - EXIT) '
        f'current_floor={current_floor}, '
        f'passenger_aboard={passenger_aboard}, '
        f'destination={destination}, '
        f'floor_queue={floor_queue}'
    )

    return updated_params
