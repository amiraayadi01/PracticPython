#Decode A Web Page Two
#Topics: Inspecting HTML on a web page

import requests
from bs4 import BeautifulSoup

url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(url)
soup = BeautifulSoup(r.text)

text_body = soup.select("div.parbase.cn_text > div.body > p")

for article in text_body[7:]:
    print(article.text)


