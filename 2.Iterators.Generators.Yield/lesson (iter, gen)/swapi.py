import requests


class SwapiPeopleIterator:
    def __init__(self):
        pass

    def __iter__(self):
        # Выполняется на входе в цикл
        self.next_url = "https://swapi.py4e.com/api/people/"
        self.people = iter([])
        return self

    def __next__(self):
        # Выполняется на каждой итерации цикла

        next_character = self._get_next_character()
        if next_character is None:
            if self.next_url is None:
                raise StopIteration
            self._get_people()

            next_character = self._get_next_character()

        return next_character  # Будеь подставляться в item

    def _get_next_character(self):
        try:
            next_character = next(self.people)
        except StopIteration:
            next_character = None
        return next_character

    def _get_people(self):
        response = requests.get(self.next_url)
        data = response.json()
        self.next_url = data["next"]
        self.people = iter(data["results"])


swapi_people = SwapiPeopleIterator()
for character in swapi_people:
    print(character)
