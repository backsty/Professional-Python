import requests


def swapi_generator():
    next_url = "https://swapi.py4e.com/api/people/"

    while next_url is not None:
        response = requests.get(next_url)
        response = response.json()
        next_url = response["next"]
        for character in response["results"]:
            yield character


swapi_pepople_tall = (
    (character["name"], character["birth_year"])
    for character in swapi_generator()
    if character["height"] not in {"unknown", "none"}
    and int(character["height"]) >= 172
)

for character in swapi_pepople_tall:
    print(character)
