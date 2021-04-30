# pip install requests
# pip install bs4

import requests
from bs4 import BeautifulSoup as bs

gitHub_user = input("Input your githib id: ")
url = "https://github.com/" + gitHub_user
r = requests.get(url)
soup = bs(r.content, "html.parser")
profile_image = soup.find('img', {'alt': 'Avatar'})['src']
print("click on the link below to see your profile image:")
print(profile_image)
