import pytest

import src.call


@pytest.fixture
def mock_happens_by_chance_true(mocker):
    mock_chance_true = mocker.patch('src.call.happens_by_chance')
    mock_chance_true.return_value = True

    return mock_chance_true


@pytest.fixture
def mock_randint_value(mocker):
    mock_random_floor = mocker.patch('src.call.randint')
    mock_random_floor.return_value = 1

    return mock_random_floor


def test_call_elevator_calling_floor(
    mock_happens_by_chance_true, mock_randint_value
):
    floor_passenger = {2: 3}

    new_called_floor = src.call.call_elevator(floor_passenger=floor_passenger)

    assert len(new_called_floor) > 0


def test_call_elevator_calling_already_called_floor(
    mock_happens_by_chance_true, mock_randint_value
):
    floor_passenger = {1: 1}

    new_called_floor = src.call.call_elevator(floor_passenger=floor_passenger)

    assert len(new_called_floor) == 0


def test_call_elevator_not_calling_floor(mocker):
    mock_chance_happens = mocker.patch('src.call.happens_by_chance')
    mock_chance_happens.return_value = False
    floor_passenger = {2: 3}

    new_called_floor = src.call.call_elevator(floor_passenger=floor_passenger)

    assert len(new_called_floor) == 0
