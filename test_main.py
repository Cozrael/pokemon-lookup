import pytest
from main import normalize_name, extract_pokemon_info, fetch_pokemon

SAMPLE_DATA = {
    "id": 1,
    "name": "bulbasaur",
    "height": 7,
    "weight": 69,
    "types": [
        {"slot": 1, "type": {"name": "grass"}},
        {"slot": 2, "type": {"name": "poison"}},
    ],
    "stats": [
        {"base_stat": 45, "stat": {"name": "hp"}},
        {"base_stat": 49, "stat": {"name": "special-attack"}},
    ],
}

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

def test_extract_pokemon_info():
    result = extract_pokemon_info(SAMPLE_DATA)
    assert result == {
        "id": 1,
        "name": "bulbasaur",
        "height": 0.7,
        "weight": 6.9,
        "types": ["grass", "poison"],
        "stats": {
            "hp": 45,
            "special-attack": 49
        }
    }

def test_fetch_pokemon_empty_name():
    with pytest.raises(ValueError, match="cannot be empty"):
        fetch_pokemon("")
