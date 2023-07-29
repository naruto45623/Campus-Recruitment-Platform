import sys
username1 = sys.argv[1]
username2 = sys.argv[2]
username3 = sys.argv[3]
username4 = sys.argv[4]

import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}

url1 = "https://www.hackerrank.com/leaderboard?filter="+username1+"&filter_on=hacker&h_r=internal-search&level=1&page=1&track=algorithms&type=practice"
url2 = "https://leetcode.com/"+username2+"/"
url3 = "https://www.codechef.com/users/"+username3
url4 = "https://www.interviewbit.com/profile/"+username4+"/"

response1 = requests.get(url1, headers=headers)
soup1 = BeautifulSoup(response1.content, 'html.parser')
score_div1 = soup1.find('div', {'class': 'table-row-column ellipsis score'})
score1 = int(float(score_div1.find('span').text))

response2 = requests.get(url2)
soup2 = BeautifulSoup(response2.content, 'html.parser')
solved_problems_div = soup2.find('div', {'class': 'mx-3 flex items-center lc-xl:mx-8'})
score2 = int(solved_problems_div.find('div', {'class': 'text-[24px] font-medium text-label-1 dark:text-dark-label-1'}).text)

response3 = requests.get(url3, headers=headers)
soup3 = BeautifulSoup(response3.content, 'html.parser')
section = soup3.find('section', {'class': 'rating-data-section problems-solved'})
score3 = 0
if section:
    fully_solved_header = section.find('h5', string=lambda s: 'Fully Solved' in s)
    if fully_solved_header:
        score3 = int(fully_solved_header.text.split('(')[1].split(')')[0])

response4= requests.get(url4, headers=headers)
soup4 = BeautifulSoup(response4.content, "html.parser")
score_element = soup4.find("div", class_="stat pull-left").find("div", class_="txt")
score4 = int(score_element.text.strip())

print(str(score1)+"/"+str(score2)+"/"+str(score3)+"/"+str(score4))