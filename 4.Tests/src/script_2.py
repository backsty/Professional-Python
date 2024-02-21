import requests
from configparser import ConfigParser


config = ConfigParser()
config.read('config.ini')


def get_yandex_token():
    my_yandex_token = config['YANDEX']['token']
    return my_yandex_token


class YandexDisc:
    def __init__(self, folder_name, my_yandex_token):
        self.token = my_yandex_token
        self.name = folder_name
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources'
        self.headers = {
            'Authorization': f'Oauth {self.token}',
            'Content-Type': 'application/json',
        }

    def create_folder(self, folder_name):
        """
        Метод для создания папки на Яндекс диске
        """
        params = {'path': folder_name}
        response = requests.put(self.url, headers=self.headers, params=params)
        if response.status_code == 201:  # Created
            print(f'\nПапка {folder_name} успешно создана на вашем Яндекс диске!\n')
        elif response.status_code == 409:  # Conflict
            print(f'\nПапка {folder_name} уже существует на вашем Яндекс диске!\n')
        else:
            print(f'\nОшибка {response.status_code} - {response.text}\n')

        return folder_name


if __name__ == '__main__':
    my_token = get_yandex_token()
    my_yandex = YandexDisc('test_dir', my_token)
    my_yandex.create_folder('test_dir')
