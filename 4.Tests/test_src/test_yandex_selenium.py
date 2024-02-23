# import unittest
# from unittest import TestCase
# from parameterized import parameterized
import pytest
from src.script_3 import get_yandex_token, AuthYandex
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# my_yandex_login_, my_yandex_password_ = get_yandex_token()
#
# chrome_driver_path = ChromeDriverManager().install()
# browser_service = Service(executable_path=chrome_driver_path)
# browser = webdriver.Chrome(service=browser_service)
#
#
# class Test_Authorize_Yandex_Pytest:
#     @pytest.mark.parametrize("login, password, expected_message", [
#         (my_yandex_login_, my_yandex_password_, "valid_success_message"),
#         ("invalid_login", "invalid_password", "invalid_error_message")
#     ])
#     def test_logpass_auth(self, login, password, expected_message):
#         auth_y = AuthYandex(login, password)
#         result = auth_y.authorize_yandex()
#         assert expected_message in result.text


class TestYandexAuthentication:
    @pytest.fixture(scope="class")
    def setup(self):
        """
        Почему-то у себя не могу пройти тесты (не может законектиться)
        """
        # chrome_driver_path = ChromeDriverManager().install()
        # browser_service = Service(executable_path=chrome_driver_path)
        # browser = webdriver.Chrome(service=browser_service)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=7gAAAAAAAAAAAAAAAAAAAAB0aGVndWFyZGlhbi5jb20%3D')
        browser = webdriver.Chrome(chrome_options=chrome_options)
        yield
        browser.quit()

    def test_successful_auth(self):
        my_yandex_login_, my_yandex_password_ = get_yandex_token()
        auth_y = AuthYandex(my_yandex_login_, my_yandex_password_)
        auth_y.authorize_yandex()

        welcome_message = WebDriverWait(auth_y.browser, 10)\
            .until(EC.presence_of_element_located((By.CLASS_NAME, 'welcome-message')))
        assert "Welcome" in welcome_message.text

    def test_yandex_auth(self):
        my_yandex_login_, my_yandex_password_ = "invalid_login", "invalid_password"
        auth_y = AuthYandex(my_yandex_login_, my_yandex_password_)
        auth_y.authorize_yandex()

        welcome_message = WebDriverWait(auth_y.browser, 10)\
            .until(EC.presence_of_element_located((By.CLASS_NAME, 'error-message')))
        assert "Error" in welcome_message.text

# class Test_Authorize_Yandex_Unittest(TestCase):
#     @parameterized.expand("login, password, expected_message", [
#         ("valid_login", "valid_password", "valid_success_message"),
#         ("invalid_login", "invalid_password", "invalid_error_message")
#     ])
#     def test_logpass_auth(self, login, password):
#         auth_y = AuthYandex(login, password)
#         result = auth_y.authorize_yandex()
#         self.assertIn("valid_success_message", result.text)
#
#     def test_authorize_yandex_invalid(self, login, password):
#         auth_y = AuthYandex(login, password)
#         result = auth_y.authorize_yandex()
#         self.assertIn("invalid_error_message", result.text)
#
#
# if __name__ == '__main__':
#     unittest.main()
