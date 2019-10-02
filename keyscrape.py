import os
import requests
from bs4 import BeautifulSoup

print("keyscrape will fetch public ssh keys from a user's account.")
print("reading config.py...")


if os.path.exists("keys"):
  os.remove("keys")

def file_read(fname):
  user_array = [line.rstrip('\n') for line in open(fname)]
  for i in user_array:
    url = "https://github.com/" + i + ".keys"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    path = "keys"
    file = open(path, "a")
    file.write(i + ":\n")
    file.write(soup.prettify())
    file.close()
    print("Fetched " + i + "'s public ssh keys from Github")

file_read("config.py")