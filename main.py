import requests
import re

def fetch_pokemon(name):
    if name == "":
        raise ValueError("Pokemon name cannot be empty")
    url = 'https://pokeapi.co/api/v2/pokemon/'

    response = requests.get(f'{url}{name}',timeout=5)
    if response.status_code == 404:
        raise ValueError("Pokemon not found")
    response.raise_for_status()

    data = response.json()
    if "id" not in data:
        raise ValueError("Invalid Pokemon.")
    return data

def normalize_name(raw_name):
    return re.sub(' +', '-', raw_name.lower().strip())

def extract_pokemon_info(data):
    pokemon_id = data["id"]
    pokemon_name = data["name"]
    height = data["height"]/10
    weight = data["weight"]/10

    type_list = []
    for type_entry in data["types"]:
        type_list.append(type_entry["type"]["name"])

    stat_dict = {}
    for stat in data["stats"]:
        stat_name = stat["stat"]["name"]
        stat_value = stat["base_stat"]
        stat_dict[stat_name] = stat_value

    return {
        "id": pokemon_id,
        "name": pokemon_name,
        "height": height,
        "weight": weight,
        "types": type_list,
        "stats": stat_dict
    }

def display_pokemon(pokemon):
    types = ", ".join(pokemon["types"])
    print(f'Id: {pokemon["id"]}\n'
          f'Name: {pokemon["name"].capitalize()}\n'
          f'Height: {pokemon["height"]}m\n'
          f'Weight: {pokemon["weight"]}kg\n'
          f'Types: {types}\n'
          f'Stats:')
    for name, value in pokemon["stats"].items():
        print(f'\t{name.capitalize().replace("-", " ")}: {value}')

def main():
    normalized_name = normalize_name(input("Enter pokemon name: "))
    try:
        data = fetch_pokemon(normalized_name)
    except ValueError as e:
        print(e)
        return
    except requests.exceptions.RequestException as e:
        print(f'Could not reach the PokéAPI, check your connection and try again ({e})')
        return

    info = extract_pokemon_info(data)
    display_pokemon(info)

if __name__ == "__main__":
    main()