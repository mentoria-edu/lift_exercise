from src.movement import set_path


def test_set_path_eq_destination_when_passenger_aboard_destination():

    passenger_aboard = 2
    floor_queue = []
    destination = [4,6]

    path = set_path(
        passenger_aboard=passenger_aboard,
        floor_queue=floor_queue,
        destination=destination
    )

    assert path == destination


def test_set_path_eq_floor_queue_when_floor_queue_and_not_passenger_aboard():
    
    passenger_aboard = 0
    floor_queue = [3,6,8]
    destination = []

    path = set_path(
        passenger_aboard=passenger_aboard,
        floor_queue=floor_queue,
        destination=destination
    )

    assert path == floor_queue


def test_seth_path_no_path_when_not_floor_queue_and_destination():
    
    passenger_aboard = 0
    floor_queue = []
    destination = []

    path = set_path(
        passenger_aboard=passenger_aboard,
        floor_queue=floor_queue,
        destination=destination
    )

    assert path == []
    