from bs4 import BeautifulSoup

import json  

from openpyxl import Workbook

wb = Workbook()

sheet = wb.active

import requests

page_source = requests.get('https://www.seniorcare.com/directory/al/hokes-bluff/')

soup = BeautifulSoup(page_source.text,'html.parser')

a = soup.prettify()  

print(a)

# result = json.loads(a)

# for data in a:
#     sheet.append(data)

wb.save("main.xlsx")