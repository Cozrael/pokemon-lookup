import requests

def fetch_pokemon(name):
    url = 'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(f'{url}{name}')
    data = response.json()
    return data

def main():
    input_name = input('Enter pokemon name: ').lower().strip().replace(" ", "-")
    data = fetch_pokemon(input_name)

    pokemon_id = data["id"]
    name = data["name"].capitalize()
    height = data["height"]/10
    weight = data["weight"]/10

    type_list = []
    for type_entry in data["types"]:
        type_list.append(type_entry["type"]["name"])
    types = ", ".join(type_list)

    print(f'Searching for: '
          f'{input_name}\n'
          f'Id: {pokemon_id}\n'
          f'Name: {name}\n'
          f'Height: {height}m\n'
          f'Weight: {weight}kg\n'
          f'Type(s): {types}\n'
          f'Stats:')

    for stat in data["stats"]:
        stat_name = stat["stat"]["name"].capitalize().replace("-", " ")
        stat_value = stat["base_stat"]
        print(f'\t{stat_name}: {stat_value}')

if __name__ == "__main__":
    main()