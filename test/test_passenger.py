import pytest

import src.passenger


@pytest.mark.parametrize('new_pass',[
    (1),
    (2),
    (3),
    (4),
    (5),
    (6)
    ])
def test_get_passenger_destination_not_0_in_ground_floor(
    new_pass
):
    current_floor = 0
    new_passenger = new_pass

    new_destination = src.passenger.get_passenger_destination(
        current_floor=current_floor,
        new_passenger=new_passenger
    )

    assert not new_destination.count(0)


@pytest.mark.parametrize('new_pass',[
    (1),
    (2),
    (3),
    (4),
    (5),
    (6)
])
def test_get_passenger_destination_0_not_ground_floor_chance_false(
    mocker,new_pass
):
    mock_chance_happens = mocker.patch('src.passenger.happens_by_chance')
    mock_chance_happens.return_value = False
    current_floor = 15
    new_passenger = new_pass

    new_destination = src.passenger.get_passenger_destination(
        current_floor=current_floor,
        new_passenger=new_passenger
    )

    assert new_destination.count(0)


@pytest.mark.parametrize('new_pass',[
    (1),
    (2),
    (3),
    (4),
    (5),
    (6)
])
def test_get_passenger_destination_not_0_not_ground_floor_chance_true(
    mocker,new_pass
):
    mock_chance_happens = mocker.patch('src.passenger.happens_by_chance')
    mock_randint = mocker.patch('src.passenger.randint')
    current_floor = 15
    new_passenger = new_pass

    mock_chance_happens.return_value = True
    mock_randint.return_value = 6

    new_destination = src.passenger.get_passenger_destination(
        current_floor=current_floor,
        new_passenger=new_passenger
    )

    print(new_destination)

    assert len(new_destination) and not new_destination.count(0)


def test_board_passanger_lift_capacity_exceeded(mocker):
    current_floor = 1 
    floor_passenger = {1:4}
    passenger_aboard = 3
    old_passenger_aboard = passenger_aboard
    floor_queue = [1]
    destination = [4,7,3]
    old_destination = destination.copy()
    mock_chance = mocker.patch('src.passenger.happens_by_chance')
    mock_chance.return_value = True

    result_board_passanger = src.passenger.board_passenger(
        current_floor=current_floor,
        floor_passenger=floor_passenger,
        passenger_aboard=passenger_aboard,
        floor_queue=floor_queue,
        destination=destination
    )

    updated_passenger_aboard = result_board_passanger['updated_passenger_aboard']
    updated_destination = result_board_passanger['updated_destination']

    assert old_destination != updated_destination and old_passenger_aboard != updated_passenger_aboard 


def test_board_passanger_lift_capacity_not_exceeded(mocker):
    current_floor = 1 
    floor_passenger = {1:3}
    old_floor_passenger = floor_passenger.copy()
    passenger_aboard = 3
    old_passenger_aboard = passenger_aboard
    floor_queue = [1]
    destination = [4,7,3]
    old_destination = destination.copy()
    mock_chance = mocker.patch('src.passenger.happens_by_chance')
    mock_chance.return_value = True

    result_board_passenger = src.passenger.board_passenger(
        current_floor=current_floor,
        floor_passenger=floor_passenger,
        passenger_aboard=passenger_aboard,
        floor_queue=floor_queue,
        destination=destination
    )

    updated_passenger_aboard = result_board_passenger['updated_passenger_aboard']
    updated_destination = result_board_passenger['updated_destination']
    updated_floor_passenger = result_board_passenger['updated_floor_passenger']

    assert old_destination != updated_destination 
    assert old_passenger_aboard != updated_passenger_aboard
    assert old_floor_passenger !=updated_floor_passenger


def test_unboard_passenger_with_passenger_to_unboard():
    passenger_aboard = 3
    old_passenger_aboard = passenger_aboard
    current_floor = 5
    destination = [5,4,3]
    old_destination = destination.copy()

    result_unboard_passenger = src.passenger.unboard_passenger(
        passenger_aboard=passenger_aboard,
        current_floor=current_floor,
        destination=destination
    )

    updated_passenger_aboard = result_unboard_passenger['updated_passenger_aboard']
    updated_destination = result_unboard_passenger['updated_destination']

    assert old_passenger_aboard != updated_passenger_aboard
    assert old_destination != updated_destination


def test_unboard_passenger_without_passenger_to_unboard():
    passenger_aboard = 3
    old_passenger_aboard = passenger_aboard
    current_floor = 6
    destination = [5,4,3]
    old_destination = destination.copy()

    result_unboard_passenger = src.passenger.unboard_passenger(
        passenger_aboard=passenger_aboard,
        current_floor=current_floor,
        destination=destination
    )

    updated_passenger_aboard = result_unboard_passenger['updated_passenger_aboard']
    updated_destination = result_unboard_passenger['updated_destination']

    assert old_passenger_aboard == updated_passenger_aboard
    assert old_destination == updated_destination

