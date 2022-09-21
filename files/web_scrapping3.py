import requests
from bs4 import BeautifulSoup

user_input = input("enter something to search:")
print("Googling....")

results = requests.get('https://www.google.com/search?q=tech%20gram%20academy' + user_input)

soup = BeautifulSoup(results.text,'html.parser')
# print(soup)

print(soup.prettify())

search = soup.select('.egMi0 kCrYT a')
print(search)

for link in search[:5]:
    print(link)