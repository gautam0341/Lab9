import requests

Pokemon_Api = "https://pokeapi.co/api/v2"


def get_Pokemon_Name_List():
    url = f"{Pokemon_Api}/pokemon?limit=1000"
    response = requests.get(url)
    if response.ok:
        data = response.json()
        return [pokemon["name"] for pokemon in data["results"]]
    else:
        response.raise_for_status()


def download_pokemon_artwork(url, path):
    response = requests.get(url)
    if response.ok:
        with open(path, "wb") as f:
            f.write(response.content)
    else:
        response.raise_for_status()
