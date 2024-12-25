from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)

driver.get('https://www.example.com')

driver.save_screenshot('screenshot.png')

driver.quit()