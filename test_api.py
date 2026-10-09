import pytest
from main import fetch_pokemon

def test_fetch_pokemon_valid_name():
    real_data = fetch_pokemon("pikachu")
    assert real_data["name"] == "pikachu"
    assert real_data["id"] == 25

def test_fetch_pokemon_invalid_name():
    with pytest.raises(ValueError, match="Pokemon not found"):
        fetch_pokemon("asdasd")

@pytest.mark.parametrize("name", [".", ".."])
def test_fetch_pokemon_special_chars(name):
    with pytest.raises(ValueError, match="Invalid Pokemon."):
        fetch_pokemon(name)
