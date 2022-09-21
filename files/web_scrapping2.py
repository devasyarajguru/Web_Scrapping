from bs4 import BeautifulSoup

import requests

from openpyxl import Workbook

wb = Workbook()

sheet = wb.active

page_source = requests.get("https://www.totallyuselesswebsites.com/")

soup =  BeautifulSoup(page_source.text,'html.parser')

# print(soup.prettify())

all_links = soup.find_all('a')

for link in all_links:
    print(link.get('href'))

wb.save("demo.xlsx")
