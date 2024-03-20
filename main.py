import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'e96a9c39f4ca1a3092a082b9ed6e7661'
HEADERS = {
    'Content-Type' : 'application/json',
    'trainer_token': TOKEN
    }

body = {
    'name': "Шрек",
    'photo': 'https://dolnikov.ru/pokemons/albums/053.png'
}

body_2 = {
    "pokemon_id": "14411",
    "name": "Прошрек",
    "photo": "https://dolnikov.ru/pokemons/albums/053.png"
}

body_3 = {
    "pokemon_id": "14411"
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADERS, json = body)

print(response.text)

response = requests.put(url = f'{URL}/pokemons', headers = HEADERS, json = body_2)

print(response.text)

response_confirm = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADERS, json=body_3)

print(response_confirm.text)