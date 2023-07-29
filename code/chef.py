import sys
username = sys.argv[1]

import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}
# URL of the CodeChef user's profile
url = "https://www.codechef.com/users/"+username

html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')

section = soup.find('section', {'class': 'rating-data-section problems-solved'})
fully_solved_count = 0
if section:
    fully_solved_header = section.find('h5', string=lambda s: 'Fully Solved' in s)
    if fully_solved_header:
        fully_solved_count = int(fully_solved_header.text.split('(')[1].split(')')[0])
print(fully_solved_count)