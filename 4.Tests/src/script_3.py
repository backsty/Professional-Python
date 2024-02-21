import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from configparser import ConfigParser


config = ConfigParser()
config.read('config.ini')


def get_yandex_token():
    my_yandex_login_ = config['YANDEX']['login']
    my_yandex_password_ = config['YANDEX']['password']
    return my_yandex_login_, my_yandex_password_


chrome_driver_path = ChromeDriverManager().install()
browser_service = Service(executable_path=chrome_driver_path)
browser = webdriver.Chrome(service=browser_service)


class AuthYandex:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def authorize_yandex(self):
        browser.get('https://passport.yandex.ru/auth/welcome')
        time.sleep(2)

        email_input = browser.find_element(by='id', value='passp-field-login')
        email_input.clear()
        email_input.send_keys(self.login)
        time.sleep(2)
        email_input.send_keys(Keys.ENTER)
        time.sleep(2)

        password_input = browser.find_element(by='id', value='passp-field-passwd')
        password_input.send_keys(self.password)
        time.sleep(2)
        password_input.send_keys(Keys.ENTER)
        time.sleep(3)

        return browser.find_element(by='class', value='Card_label__AG2MY')


if __name__ == '__main__':
    my_yandex_login, my_yandex_password = get_yandex_token()
    auth_y = AuthYandex(my_yandex_login, my_yandex_password)
    auth_y.authorize_yandex()

    browser.close()
    browser.quit()