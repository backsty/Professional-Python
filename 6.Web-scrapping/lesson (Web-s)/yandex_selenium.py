"""
ul id="search-result"
li
https://yandex.ru/search/?text=%D1%87%D1%82%D0%BE+%D0%BD%D0%B8%D0%B1%D1%83%D0%B4%D1%8C&search_source=dzen_desktop_safe&lr=39
"""

import bs4
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def wait_element(browser, delay_seconds=1, by=By.TAG_NAME, value=None):
    return WebDriverWait(browser, delay_seconds).until(
        expected_conditions.presence_of_element_located((by, value))
    )


path = ChromeDriverManager().install()
browser_service = Service(executable_path=path)
service = Service(executable_path=path)
browser = Chrome(service=service)

browser.find_element(By.ID, "search-result")

browser.get("https://yandex.ru/")
browser.get(
    "https://yandex.ru/search/?text=%D1%87%D1%82%D0%BE+%D0%BD%D0%B8%D0%B1%D1%83%D1%83%D0%B4%D1%8C&search_source=dzen_desktop_safe&lr=39"
)

ul = wait_element(browser, 5, By.ID, "search-result")

html_data = browser.page_source

soup = bs4.BeautifulSoup(html_data, "lxml")

ul_tag = soup.find("ul", id="search-result")
li_tags = ul_tag.find_all("li")
for tag in li_tags:
    print(tag.text.strip())
