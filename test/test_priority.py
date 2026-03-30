import src.priority


def test_check_priority_prioritize_delivering_if_passenger_aboard():
    passenger_aboard = 5
    floor_queue = [5, 2, 18, 12]
    destination = [18, 12, 2, 6, 8]
    old_destination = destination.copy()

    result = src.priority.check_priority(
        passenger_aboard=passenger_aboard,
        floor_queue=floor_queue,
        destination=destination,
    )

    new_destination = result['sorted_destination']

    assert new_destination[0] != old_destination[0]


def test_check_priority_prioritize_boarding_if_not_passenger_aboard():

    passenger_aboard = 0
    floor_queue = [5, 2, 18, 12]
    destination = [18, 12, 2, 6, 8]
    old_floor_queue = floor_queue.copy()

    result = src.priority.check_priority(
        passenger_aboard=passenger_aboard,
        floor_queue=floor_queue,
        destination=destination,
    )

    new_floor_queue = result['sorted_queue']

    assert new_floor_queue[0] != old_floor_queue[0]
