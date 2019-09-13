import ssl
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

WORDS = []
with open("large.txt", "r") as file:
    for line in file.readlines():
        WORDS.append(line.rstrip())

file = open("large.txt", "a")


def insert(str):
    str = str.lower()
    if str in WORDS:
        return False
    WORDS.append(str)
    file.write(str)
    file.write("\n")
    return True


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter url - ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('p')

t = 0
c = 0
for tag in tags:
    words = tag.text.split(' ')
    for word in words:
        if len(word) > 1 and word.isalpha():
            t += 1
            if insert(word):
                c += 1

file.close()
print(f"{c} out of {t} words inserted")
