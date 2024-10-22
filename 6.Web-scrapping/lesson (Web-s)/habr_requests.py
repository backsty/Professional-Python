"""
div class="tm-articles-list"
<article>
<h2 class="tm-title tm-title_h2">
    <a href="/ru/articles/791038/" data-test-id="article-snippet-title-link" data-article-link="true" class="tm-title__link">
        <span>СЕО с вашей прошлой работы: к тебе придет ФСБ</span>
    </a>
    </h2>
<time datetime="2024-02-02T16:55:12.000Z" title="2024-02-02, 18:55">5 минут назад</time>
id="post-content-body"
"""

import bs4
import fake_headers
import requests

URL = "https://habr.com/ru/articles/"


def gen_headers():
    headers_gen = fake_headers.Headers(os="win", browser="chrome")
    return headers_gen.generate()


response = requests.get(URL, headers=gen_headers())
main_html = response.text
main_page = bs4.BeautifulSoup(main_html, "lxml")

article_list_tag = main_page.find("div", class_="tm-articles-list")

articles_tags = article_list_tag.find_all("article")

articles_data = []

for article_tag in articles_tags:
    h2_tag = article_tag.find("h2", class_="tm-title tm-title_h2")
    a_tag = h2_tag.find("a")
    tag_span = h2_tag.find("span")
    time_tag = article_tag.find("time")

    link_relative = a_tag["href"]
    link_absolute = f"https://habr.com{link_relative}"
    header = tag_span.text.strip()
    publication_time = time_tag["datetime"]

    response = requests.get(link_absolute, headers=gen_headers())
    article_html = response.text
    article_page = bs4.BeautifulSoup(article_html, "lxml")
    article_body_tag = article_page.find(id="post-content-body")
    article_text = article_body_tag.text.strip()

    articles_data.append(
        {
            "header": header,
            "link": link_absolute,
            "publication_time": publication_time,
            "text": article_text,
        }
    )
