import pytest


@pytest.fixture(autouse=True)
def no_sleep(monkeypatch):
    monkeypatch.setattr('src.call.sleep', lambda x: None)
    monkeypatch.setattr('src.movement.sleep', lambda x: None)
    monkeypatch.setattr('src.passenger.sleep', lambda x: None)
