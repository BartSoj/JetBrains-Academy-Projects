import os
import sys
import requests
from bs4 import BeautifulSoup
from colorama import Fore

path = sys.argv[1]
if not os.path.exists(path):
    os.mkdir(path)
url = []
while True:
    url.append(input())
    if url[-1] == "exit":
        break
    elif url[-1] == "back":
        url = url[:-2]
    try:
        with open(path + "/" + url[-1], "r") as f:
            for line in f.readlines():
                print(line, end="")
    except OSError:
        if "." not in url[-1]:
            print("Error: Incorrect URL")
        else:
            r = requests.get(url[-1] if url[-1].startswith("https://") else "https://" + url[-1])
            text = BeautifulSoup(r.content, "html.parser").get_text()
            print(Fore.BLUE + text)
            with open(path + "/" + url[-1][:url[-1].rfind(".")], "w") as f:
                print(Fore.BLUE + text, file=f)
