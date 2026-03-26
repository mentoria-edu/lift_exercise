import pytest

import src.passenger


@pytest.fixture
def mock_happens_by_chance_true(mocker):
    mock_chance_true = mocker.patch('src.passenger.happens_by_chance')
    mock_chance_true.return_value = True

    return mock_chance_true


@pytest.fixture
def mock_happens_by_chance_false(mocker):
    mock_chance_false = mocker.patch('src.passenger.happens_by_chance')
    mock_chance_false.return_value = False

    return mock_chance_false


@pytest.fixture(params=list(range(1, 6 + 1)))
def new_passenger_amount(request):
    return request.param


@pytest.fixture(params=list(range(1, 18 + 1)))
def current_floor_parametrize(request):
    return request.param


def test_get_passenger_destination_not_to_ground_floor_when_lift_is_at_ground(
    new_passenger_amount
):
    current_floor = 0

    new_destination = src.passenger.get_passenger_destination(
        current_floor=current_floor,
        new_passenger=new_passenger_amount
    )

    assert new_destination.count(0) == 0


def test_get_passenger_destination_to_ground_floor_when_lift_is_above(
    mock_happens_by_chance_false,
    new_passenger_amount,
    current_floor_parametrize
):
    new_passenger = new_passenger_amount
    current_floor = current_floor_parametrize

    new_destination = src.passenger.get_passenger_destination(
        current_floor=current_floor, new_passenger=new_passenger
    )

    assert new_destination.count(0) == new_passenger


def test_get_passenger_destination_not_to_ground_floor_when_lift_is_above(
    mocker,
    mock_happens_by_chance_true,
    new_passenger_amount,
    current_floor_parametrize
):
    new_passenger = new_passenger_amount
    current_floor = current_floor_parametrize
    mock_randint = mocker.patch('src.passenger.randint')
    mock_randint.return_value = 6

    new_destination = src.passenger.get_passenger_destination(
        current_floor=current_floor, new_passenger=new_passenger
    )

    assert len(new_destination) > 0
    assert new_destination.count(0) == 0


def test_board_passanger_if_lift_capacity_exceeded(
        mock_happens_by_chance_true
    ):
    current_floor = 1
    floor_passenger = {1: 4}
    passenger_aboard = 3
    old_passenger_aboard = passenger_aboard
    floor_queue = [1]
    destination = [4, 7, 3]
    old_destination = destination.copy()

    result_board_passanger = src.passenger.board_passenger(
        current_floor=current_floor,
        floor_passenger=floor_passenger,
        passenger_aboard=passenger_aboard,
        floor_queue=floor_queue,
        destination=destination,
    )

    updated_passenger_aboard = result_board_passanger[
        'updated_passenger_aboard'
    ]
    updated_destination = result_board_passanger['updated_destination']

    assert old_destination != updated_destination
    assert old_passenger_aboard != updated_passenger_aboard


def test_board_passanger_if_lift_capacity_not_exceeded(
        mock_happens_by_chance_true
):
    current_floor = 1
    floor_passenger = {1: 3}
    old_floor_passenger = floor_passenger.copy()
    passenger_aboard = 3
    old_passenger_aboard = passenger_aboard
    floor_queue = [1]
    destination = [4, 7, 3]
    old_destination = destination.copy()

    result_board_passenger = src.passenger.board_passenger(
        current_floor=current_floor,
        floor_passenger=floor_passenger,
        passenger_aboard=passenger_aboard,
        floor_queue=floor_queue,
        destination=destination,
    )

    updated_passenger_aboard = result_board_passenger[
        'updated_passenger_aboard'
    ]
    updated_destination = result_board_passenger['updated_destination']
    updated_floor_passenger = result_board_passenger['updated_floor_passenger']

    assert old_destination != updated_destination
    assert old_passenger_aboard != updated_passenger_aboard
    assert old_floor_passenger != updated_floor_passenger


def test_unboard_passenger_with_passenger_to_unboard_at_current_floor():
    passenger_aboard = 3
    old_passenger_aboard = passenger_aboard
    current_floor = 5
    destination = [5, 4, 3]
    old_destination = destination.copy()

    result_unboard_passenger = src.passenger.unboard_passenger(
        passenger_aboard=passenger_aboard,
        current_floor=current_floor,
        destination=destination,
    )

    updated_passenger_aboard = result_unboard_passenger[
        'updated_passenger_aboard'
    ]
    updated_destination = result_unboard_passenger['updated_destination']

    assert old_passenger_aboard != updated_passenger_aboard
    assert old_destination != updated_destination


def test_unboard_passenger_without_passenger_to_unboard_at_current_floor():
    passenger_aboard = 3
    old_passenger_aboard = passenger_aboard
    current_floor = 6
    destination = [5, 4, 3]
    old_destination = destination.copy()

    result_unboard_passenger = src.passenger.unboard_passenger(
        passenger_aboard=passenger_aboard,
        current_floor=current_floor,
        destination=destination,
    )

    updated_passenger_aboard = result_unboard_passenger[
        'updated_passenger_aboard'
    ]
    updated_destination = result_unboard_passenger['updated_destination']

    assert old_passenger_aboard == updated_passenger_aboard
    assert old_destination == updated_destination
