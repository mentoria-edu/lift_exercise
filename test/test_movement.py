import src.movement


def test_set_path_equals_destination_when_passenger_aboard():

    passenger_aboard = 2
    floor_queue = []
    destination = [4, 6]

    lift_path = src.movement.set_path(
        passenger_aboard=passenger_aboard,
        floor_queue=floor_queue,
        destination=destination,
    )

    assert lift_path == destination


def test_set_path_equals_floor_queue_when_not_passenger_aboard():

    passenger_aboard = 0
    floor_queue = [3, 6, 8]
    destination = []

    lift_path = src.movement.set_path(
        passenger_aboard=passenger_aboard,
        floor_queue=floor_queue,
        destination=destination,
    )

    assert lift_path == floor_queue


def test_seth_path_returns_empty_when_no_floor_queue_and_no_destination():

    passenger_aboard = 0
    floor_queue = []
    destination = []

    lift_path = src.movement.set_path(
        passenger_aboard=passenger_aboard,
        floor_queue=floor_queue,
        destination=destination,
    )

    assert lift_path == []


def test_stop_lift_with_passengers_to_unboard_at_current_floor():
    current_floor = 1
    floor_passenger = {3: 1}
    passenger_aboard = 4
    old_passenger_aboard = passenger_aboard
    floor_queue = [3]
    destination = [6, 0, 1, 2]
    old_destination = destination.copy()

    result_stop_lift = src.movement.stop_lift(
        current_floor=current_floor,
        floor_passenger=floor_passenger,
        passenger_aboard=passenger_aboard,
        floor_queue=floor_queue,
        destination=destination,
    )

    new_passenger_aboard = result_stop_lift['updated_passenger_aboard']
    new_destination = result_stop_lift['updated_destination']

    assert new_passenger_aboard != old_passenger_aboard
    assert new_destination != old_destination
