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
    mocker,
    new_pass
):
    mock_sleep = mocker.patch('src.passenger.sleep')
    mock_sleep.return_value = None
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
    mock_sleep = mocker.patch('src.passenger.sleep')
    mock_sleep.return_value = None
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
    mock_sleep = mocker.patch('src.passenger.sleep')
    mock_chance_happens = mocker.patch('src.passenger.happens_by_chance')
    mock_randint = mocker.patch('src.passenger.randint')
    current_floor = 15
    new_passenger = new_pass

    mock_sleep.return_value = None
    mock_chance_happens.return_value = True
    mock_randint.return_value = 6

    new_destination = src.passenger.get_passenger_destination(
        current_floor=current_floor,
        new_passenger=new_passenger
    )

    print(new_destination)

    assert len(new_destination) and not new_destination.count(0)