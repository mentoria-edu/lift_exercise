import src.call


def test_call_elevator_calling_floor(mocker):
    mock_chance_happens = mocker.patch('src.call.happens_by_chance')
    mock_random_floor = mocker.patch('src.call.randint')
    mock_chance_happens.return_value = True
    mock_random_floor.return_value = 1
    floor_passenger = {2:3}

    new_floor_passenger = src.call.call_elevator(
        floor_passenger=floor_passenger
    )

    assert new_floor_passenger


def test_call_elevator_calling_already_called_floor(mocker):
    mock_chance_happens = mocker.patch('src.call.happens_by_chance')
    mock_random_floor = mocker.patch('src.call.randint')
    mock_chance_happens.return_value = True
    mock_random_floor.return_value = 1
    current_floor_passenger = {1:1}

    new_floor_passenger = src.call.call_elevator(
        floor_passenger=current_floor_passenger
    )

    assert not new_floor_passenger


def test_call_elevator_not_calling_floor(mocker):
    mock_chance_happens = mocker.patch('src.call.happens_by_chance')
    mock_random_floor = mocker.patch('src.call.randint')
    mock_chance_happens.return_value = False
    mock_random_floor.return_value = 1
    floor_passenger = {2:3}

    new_floor_passenger = src.call.call_elevator(
        floor_passenger=floor_passenger
    )

    assert not new_floor_passenger
