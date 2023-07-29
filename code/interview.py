import sys
username = sys.argv[1]

import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}

# Make a GET request to your InterviewBit profile page
response = requests.get(f"https://www.interviewbit.com/profile/{username}/")

# Parse the HTML content with Beautiful Soup
soup = BeautifulSoup(response.content, "html.parser")

# Find the div element containing your score and extract the score text
score_element = soup.find("div", class_="stat pull-left").find("div", class_="txt")
score = score_element.text.strip()

print(score)