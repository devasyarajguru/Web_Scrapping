import re

import requests


def find_links(page_source):
    regex= re.compile(r'<a href="(.+?)" target')
    result1 = regex.findall(page_source)
    return result

result =requests.get('https://www.totallyuselesswebsites.com/')

links = find_links(result.text)
print(links)

top_links = links[0:5]
print(top_links)

# print(result.text)

