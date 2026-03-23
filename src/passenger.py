from random import randint, sample
from time import sleep

from src.chance import happens_by_chance
from src.constant import FLOOR_AMOUNT, LIFT_CAPACITY
from src.logger_config import debug, info


def register_floor_passenger(
    called_floor: int
) -> dict:

    floor_passenger = {}
    passenger_amount = randint(1, 6)

    floor_passenger.update({int(called_floor):passenger_amount})

    return floor_passenger


def get_passenger_destination(
	current_floor: int,
    new_passenger: int
) -> list:

	new_destination = []
	floor_amount=FLOOR_AMOUNT
	chance = 0.5

	if current_floor == 0:

		debug(
			'(func get_passenger_destination) '
			'current_floor is 0'
		)

		new_destination = sample(
			range(1,floor_amount),
			new_passenger
		)

		new_destination_string = ', '.join(map(str, set(new_destination)))

		sleep(2)

		info(
			'The passenger boarded '
			f'is heading towards floor no. {new_destination_string}'
			if new_passenger == 1
			else
			f'{new_passenger} passengers boarded '
			f'are heading towards floors no. {new_destination_string}'
		)

	if current_floor != 0:

		debug(
			'(func get_passenger_destination) '
			'current_floor is not 0'
		)

		for passenger in range(new_passenger):

			chance_happened = happens_by_chance(chance_modifier=chance)

			if chance_happened:

				new_destination.append(
					randint(0, current_floor-1)
				)

			if not chance_happened:
				
				new_destination.append(0)

		sleep(2)

		new_destination_string = ', '.join(map(str, set(new_destination)))

		info(
			'The passenger boarded '
			f'is heading towards floor no.: {new_destination_string}'
			if new_passenger == 1
			else
			f'{new_passenger} passengers boarded '
			f'are heading towards floors no.: {new_destination_string}'
		)

	return new_destination


def board_passenger(
	current_floor: int,
	floor_passenger: dict,
	passenger_aboard: int,
	floor_queue: list,
	destination: list
) -> dict:

	new_passenger = 0
	updated_passenger_aboard = passenger_aboard
	updated_destination = destination.copy()
	lift_capacity = LIFT_CAPACITY

	passenger_amount = floor_passenger.get(current_floor)

	if updated_passenger_aboard + passenger_amount > lift_capacity:

		new_passenger = lift_capacity - updated_passenger_aboard
		updated_passenger_aboard += new_passenger
		floor_passenger[current_floor] -= new_passenger

		info(
			f'The lift is full, {passenger_amount} passengers at '
			f'floor no. {current_floor} '
			'will have to wait' if new_passenger == 0
			else
			f'{new_passenger} out of {passenger_amount} passengers have '+
			'boarded. The remaining will have to wait.'
		)

		sleep(3)

	if updated_passenger_aboard + passenger_amount <= lift_capacity:

		new_passenger = passenger_amount
		updated_passenger_aboard += new_passenger
		info(
			f'{new_passenger} passenger(s) at the '
            f'floor no. {current_floor} have boarded the lift.'
			if current_floor != 0
            else
			f'All {new_passenger} passenger(s) at the '
            'ground floor have boarded the lift.'
		)

		sleep(3)

		floor_passenger.pop(current_floor)
		floor_queue.remove(current_floor)

	updated_destination.extend(
		get_passenger_destination(
			current_floor=current_floor,
			new_passenger=new_passenger
		)
	)

	updated_params = {
		'updated_floor_passenger':floor_passenger,
		'updated_passenger_aboard':updated_passenger_aboard,
		'updated_destination':updated_destination,
		'updated_floor_queue':floor_queue
		}


	return updated_params


def unboard_passenger(
    passenger_aboard: int,
    current_floor: int,
	destination: list
) -> dict:

	updated_passenger_aboard = passenger_aboard
	updated_destination = []

	passengers_to_unboard = destination.count(current_floor)

	if passengers_to_unboard == 0:

		return {
            'updated_passenger_aboard': passenger_aboard,
            'updated_destination': destination
        }

	info(
		f'{passengers_to_unboard} passenger(s) unboarded the lift'
	)
	sleep(2)

	updated_passenger_aboard -= passengers_to_unboard
	
	for floor in destination:
		
		if floor != current_floor:
			
			updated_destination.append(floor)

	updated_params = {
		'updated_passenger_aboard':updated_passenger_aboard,
		'updated_destination':updated_destination
	}

	return updated_params
