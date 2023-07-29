import requests

url = "https://leetcode-stats-api.herokuapp.com/dharmikbanka23"
response = requests.get(url)
data = response.json()

total_solved = data['totalSolved']

print(total_solved)