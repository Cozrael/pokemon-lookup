import requests

def fetch_pokemon(pokemon):
    url = 'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(f'{url}{pokemon}')
    data = response.json()
    return data

def main():
    pokemon_name = "pikachu"
    data = fetch_pokemon(pokemon_name)
    print(f'Id: {data["id"]}, Name: {data["name"]}, Height: {data["height"]}')

if __name__ == "__main__":
    main()