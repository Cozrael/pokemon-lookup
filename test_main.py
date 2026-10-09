import pytest
from main import normalize_name

@pytest.mark.parametrize("name, expected", [
    ("Pikachu", "pikachu"),
    ("    Pikachu  ", "pikachu"),
    ("mr mime", "mr-mime"),
    ("mr  mime", "mr-mime"),
    (" Mr miMe", "mr-mime"),
    ("mr-mime", "mr-mime"),
    ("", "")
])

def test_normalize_name(name, expected):
    assert normalize_name(name) == expected

