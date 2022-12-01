#Write to a file
#Topics: Writing to a file, Gotchas and Warnings

import requests
from bs4 import BeautifulSoup

url = "http://www.nytimes.com"
r = requests.get(url)
soup = BeautifulSoup(r.text)

with open('newfile.txt', 'w') as file:
    for story_heading in soup.find_all(class_="story-heading"):
        if story_heading.a:
            file.write(story_heading.text.replace("\n", " ").strip())
        else:
            file.write(story_heading.contents[0].strip())
