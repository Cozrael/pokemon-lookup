# Pokemon Lookup

A command-line tool written in Python that fetches Pokémon data from the [PokéAPI](https://pokeapi.co/) and displays it in the terminal.

## Status

Work in progress. The core functionality works; error handling and tests are still being added.

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
Searching for: pikachu
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

## Features

- Look up a Pokémon by name
- Displays id, name, height (m), weight (kg), types and base stats
- Supports Pokémon with multiple types (e.g. `charizard`)
- Input normalization (case-insensitive, trims spaces)
- Code separated into fetching, data extraction and display functions

## Project structure

| Function | Responsibility |
|---|---|
| `normalize_name` | Cleans up the user input |
| `fetch_pokemon` | Requests data from the PokéAPI |
| `extract_pokemon_info` | Turns the raw JSON into a simple dictionary (no printing) |
| `display_pokemon` | Formats and prints the result |

## Planned features

- Error handling (unknown Pokémon, no internet connection, request timeout)
- Unit tests for data extraction (pytest, no network needed)
- API tests (valid and invalid requests)