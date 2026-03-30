import pytest

import src.chance


@pytest.fixture
def mock_random_function_value(mocker):
    mock_random_value = mocker.patch('src.chance.random')
    mock_random_value.return_value = 0.2


@pytest.mark.parametrize('chance_modifier', [(1.0), (1.1), (-0.1), (2)])
def test_if_happens_by_chance_raises_error_with_invalid_entry(chance_modifier):
    with pytest.raises(ValueError):
        src.chance.happens_by_chance(chance_modifier=chance_modifier)


def test_happens_by_chance_true(mock_random_function_value):
    chance_modifier = 0.5

    happened = src.chance.happens_by_chance(chance_modifier=chance_modifier)

    assert happened == True


def test_happens_by_chance_false(mock_random_function_value):
    chance_modifier = 0.1

    happened = src.chance.happens_by_chance(chance_modifier=chance_modifier)

    assert happened == False
