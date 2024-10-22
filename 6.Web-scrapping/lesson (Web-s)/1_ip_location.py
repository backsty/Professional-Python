"""
<span class="table-ip4-home">
                                       93.109.178.202                                    </span>
"""

import bs4
import requests

URL = "https://www.iplocation.net/"

response = requests.get(URL)
html_data = response.text

soup = bs4.BeautifulSoup(html_data, "lxml")
span_tag = soup.find("span", class_="table-ip4-home")
ip_address = span_tag.text
ip_address = ip_address.strip()
print(f"{ip_address=}")
