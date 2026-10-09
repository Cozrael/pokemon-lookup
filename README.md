# Pokemon Lookup

A command-line tool written in Python that fetches Pokémon data from the [PokéAPI](https://pokeapi.co/) and displays it in the terminal.

## Status

Complete. Core functionality, error handling and automated tests are done.

## Requirements

- Python 3.10 or newer
- Dependencies listed in `requirements.txt`

## Setup

```
pip install -r requirements.txt
```

## How to run

```
python main.py
```

Enter a Pokémon name when prompted. The input is case-insensitive, ignores extra spaces, and converts spaces to hyphens (e.g. `Mr Mime` becomes `mr-mime`).

## Example

```
Enter pokemon name: pikachu
Id: 25
Name: Pikachu
Height: 0.4m
Weight: 6.0kg
Types: electric
Stats:
	Hp: 35
	Attack: 55
	Defense: 40
	Special attack: 50
	Special defense: 50
	Speed: 90
```

Unknown Pokémon:

```
Enter pokemon name: asdasd
Pokemon not found
```

## Features

- Look up a Pokémon by name
- Displays id, name, height (m), weight (kg), types and base stats
- Supports Pokémon with multiple types (e.g. `charizard`)
- Input normalization (case-insensitive, trims and collapses spaces)
- Error handling:
  - empty input
  - unknown Pokémon (HTTP 404)
  - invalid responses (e.g. inputs like `.` or `..`)
  - network errors, server errors and request timeout (5 seconds)
- Code separated into fetching, data extraction and display functions
- Automated tests with pytest

## Running the tests

```
pip install -r requirements.txt
pytest -v
```

The test suite has two parts:

- `test_main.py`: unit tests that run without a network connection
  - `normalize_name` (parametrized: case, extra spaces, hyphens, empty input)
  - `extract_pokemon_info` (using a hand-written sample of the API response)
  - `fetch_pokemon` input validation (`pytest.raises`)
- `test_api.py`: API tests that call the real PokéAPI
  - existing Pokémon returns the expected data
  - unknown Pokémon raises an error (404)
  - invalid inputs (`.`, `..`) raise an error

Note: the API tests need an internet connection. If they fail, check your connection and the PokéAPI status before looking for a bug in the code.

## Project structure

| File / function | Responsibility |
|---|---|
| `main.py` | The application |
| `normalize_name` | Cleans up the user input |
| `fetch_pokemon` | Requests data from the PokéAPI, raises errors on failure |
| `extract_pokemon_info` | Turns the raw JSON into a simple dictionary (no printing) |
| `display_pokemon` | Formats and prints the result |
| `main` | Connects the steps and shows error messages to the user |
| `test_main.py` | Unit tests (no network) |
| `test_api.py` | API tests (real requests) |

## Possible improvements

- Mock `requests.get` so that all tests can run offline
- Run the tests automatically with GitHub Actions
- Compare two Pokémon