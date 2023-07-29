from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\Chrome Driver\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.hackerrank.com/leaderboard?filter=dharmikbanka23&filter_on=hacker&h_r=internal-search&level=1&page=1&track=algorithms&type=practice")

wait = WebDriverWait(driver, 10)
score_div = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.table-row-wrapper > div:nth-child(1) > div:nth-child(4) > span")))

print("Score: ", score_div.text)

driver.quit()