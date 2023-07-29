import sys
username = sys.argv[1]

import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}

#112.0.5615.49 Chrome Latest Version

url = "https://www.hackerrank.com/leaderboard?filter="+username+"&filter_on=hacker&h_r=internal-search&level=1&page=1&track=algorithms&type=practice"

response = requests.get(url, headers=headers)
#print(response.status_code)  # should be 200

soup = BeautifulSoup(response.content, 'html.parser')
#print(soup.prettify())  # print the parsed HTML for inspection

score_div = soup.find('div', {'class': 'table-row-column ellipsis score'})
#print(score_div)  # print the score div for inspection

score = score_div.find('span').text
print(score)  # print the score for verification