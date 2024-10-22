import requests
import json
import logging
from fake_headers import Headers
from bs4 import BeautifulSoup
from main_3 import logger


logging.basicConfig(level=logging.INFO)


@logger("log_1.log")
def gen_fake_headers():
    """
    This function generate fake headers for the request.

    :param: None
    :return: headers_gen
    """
    headers_gen = Headers(os="win", browser="chrome").generate()
    return headers_gen


@logger("log_2.log")
def extract_vacancies(query_list: list):
    """
    This function extract job vacancies from the hh.ru website and save the results to a json file.

    :param: query_list: A list of queries (keywords) to search for job vacancies.
    :return: None
    """

    vacancies = {}
    vacancies_list = []

    query_join = '+'.join(query_list)
    url = f"https://spb.hh.ru/search/vacancy?text={query_join}&area=1&area=2"

    response = requests.get(url=url, headers=gen_fake_headers())

    if response.status_code != 200:
        logging.error("Failed to fetch the page!")
        return

    soup = BeautifulSoup(response.content, "lxml")
    try:
        page_count = int(soup.find("div", attrs={"class":"pager"}).find_all("span", recursive=False)[-1].find("a").find("span").text)
    except AttributeError:
        page_count = 1

    for page in range(page_count):
        try:
            response_page = requests.get(url=url+f"&page={page}", headers=gen_fake_headers())
            if response_page.status_code != 200:
                logging.error(f"Failed to fetch the page {page}!")
                continue
            soup_vacancies = BeautifulSoup(response_page.content, "lxml")
            vacancies_list_tag = soup_vacancies.find("div", attrs={"data-qa": "vacancy-serp__results"})
            vacancy_tag = vacancies_list_tag.find_all("div", class_="vacancy-serp-item__layout")

            for tag in vacancy_tag:
                title = tag.find("span", class_="serp-item__title").text
                link = tag.find("a", class_="bloko-link")["href"]
                company_tag = tag.find("div", class_="vacancy-serp-item__meta-info-company")
                company = " ".join(company_tag.text.split('\xa0'))
                city_tag = tag.find_all("div", class_="bloko-text")
                city = " ".join(city_tag[1].text.split('\xa0'))
                salary_tag = tag.find("span", class_="bloko-header-section-2")
                # description = tag.find("div", class_="g-user-content").text.lower()
                if salary_tag is not None:
                    salary = " ".join(salary_tag.text.split('\u202f'))
                else:
                    salary = "Не указана"
                # vacancies.setdefault(title, {"link": link, "company": company, "city": city, "salary": salary})
                vacancies_list.append({"title": title, "link": link, "company": company, "city": city, "salary": salary})
        except Exception as e:
            logging.error(f"Failed to fetch the page {page}! {e}")
            continue

    json_obj = json.dumps(vacancies_list, ensure_ascii=False, indent=4)
    with open("vacancies.json", "w", encoding="utf-8") as file:
        file.write(json_obj)

    logging.info("Парсинг завершен. Результаты сохранены в файле vacancies.json.")
    print(f"Добавлено {len(vacancies_list)} вакансий.")


if __name__ == "__main__":
    extract_vacancies(['python', 'django', 'flask'])
