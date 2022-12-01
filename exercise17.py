import requests
from bs4 import BeautifulSoup
url = 'https://www.nytimes.com//'
r = requests.get(url)
title_list = []
soup = BeautifulSoup(r.text)
title = soup.find_all('h2', {'class':'story-heading'})
for row in title:
    title_list.append(row.text)

print(title_list)
