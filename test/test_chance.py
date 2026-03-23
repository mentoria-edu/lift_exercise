import pytest

import src.chance


@pytest.mark.parametrize('chance_mod',[
    (1.0),
    (1.1),
    (-0.1),
    (2)
])
def test_if_happens_by_chance_raises_error_with_invalid_entry(
    chance_mod
):
    with pytest.raises(ValueError):
        src.chance.happens_by_chance(
            chance_modifier=chance_mod
        )


def test_happens_by_chance_true(mocker):
    mock_random = mocker.patch('src.chance.random')
    mock_random.return_value = 0.2

    happened = src.chance.happens_by_chance(
        chance_modifier=0.5
    )

    assert happened


def test_happens_by_chance_false(mocker):
    mock_random = mocker.patch('src.chance.random')
    mock_random.return_value = 0.2

    happened = src.chance.happens_by_chance(
        chance_modifier=0.1
    )

    assert not happened
