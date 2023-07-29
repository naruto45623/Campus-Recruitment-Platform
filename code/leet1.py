import sys
username = sys.argv[1]

import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}

# specify the url of the user's profile page
url = "https://leetcode.com/"+username+"/"

# make a GET request to the url and get the HTML content
response = requests.get(url)
html_content = response.content

# create a BeautifulSoup object with the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# find the div element containing the number of solved problems
solved_problems_div = soup.find('div', {'class': 'mx-3 flex items-center lc-xl:mx-8'})

# get the number of solved problems from the div
num_solved_problems = int(solved_problems_div.find('div', {'class': 'text-[24px] font-medium text-label-1 dark:text-dark-label-1'}).text)

print(num_solved_problems)