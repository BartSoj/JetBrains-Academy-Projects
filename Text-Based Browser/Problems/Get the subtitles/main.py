import requests

from bs4 import BeautifulSoup

n = int(input())
soup = BeautifulSoup(requests.get(input()).content, "html.parser")
print(soup.find_all("h2")[n].text)
