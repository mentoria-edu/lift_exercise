import src.movement


def test_set_path_eq_destination_when_passenger_aboard_destination():

    passenger_aboard = 2
    floor_queue = []
    destination = [4,6]

    path = src.movement.set_path(
        passenger_aboard=passenger_aboard,
        floor_queue=floor_queue,
        destination=destination
    )

    assert path == destination


def test_set_path_eq_floor_queue_when_floor_queue_and_not_passenger_aboard():
    
    passenger_aboard = 0
    floor_queue = [3,6,8]
    destination = []

    path = src.movement.set_path(
        passenger_aboard=passenger_aboard,
        floor_queue=floor_queue,
        destination=destination
    )

    assert path == floor_queue


def test_seth_path_no_path_when_not_floor_queue_and_destination():
    
    passenger_aboard = 0
    floor_queue = []
    destination = []

    path = src.movement.set_path(
        passenger_aboard=passenger_aboard,
        floor_queue=floor_queue,
        destination=destination
    )

    assert path == []


def test_stop_lift_with_passenger_to_unboard():
    current_floor = 1
    floor_passenger = {3:1}
    passenger_aboard = 4
    old_passenger_aboard = passenger_aboard
    floor_queue = [3]
    destination = [6,0,1,2]
    old_destination = destination.copy()

    result_stop_lift = src.movement.stop_lift(
        current_floor=current_floor,
        floor_passenger=floor_passenger,
        passenger_aboard=passenger_aboard,
        floor_queue=floor_queue,
        destination=destination
    )

    new_passenger_aboard = result_stop_lift['updated_passenger_aboard']
    new_destination = result_stop_lift['updated_destination']

    assert new_passenger_aboard != old_passenger_aboard
    assert new_destination != old_destination
