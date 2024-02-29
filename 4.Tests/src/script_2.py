import requests
from configparser import ConfigParser
import logging


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


config = ConfigParser()
config.read('C:/Users/Shala/OneDrive/Рабочий стол/Professional Python/py-homeworks-advanced/4.Tests/config.ini')


def get_yandex_token():
    my_token_ = config['YANDEX']['token']
    return my_token_


URL = 'https://cloud-api.yandex.net/v1/disk/resources'


def create_folder(folder_name, token):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'OAuth {token}',
    }
    response = requests.put(f'{URL}?path={folder_name}', headers=headers)
    logging.info(f'Folder creation response: {response.text}')
    return response


def get_folder_info(folder_name, token):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'OAuth {token}',
    }
    result = requests.get(f'{URL}?path={folder_name}', headers=headers)
    logging.info(f'Folder info response: {result.text}')
    return result


if __name__ == '__main__':
    my_token = get_yandex_token()
    logging.info('Creating a new folder on Yandex.Disk')
    create_folder('test_dir', my_token)
    get_folder_info('test_dir', my_token)
