from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import *
from time import sleep
from datetime import datetime
import keyboard
from bs4 import BeautifulSoup
import quickstart
import re
import getPath
from urllib.parse import urljoin
import random_name_generator
import get_photo_directory_filenames


firefox_profile_directory = 'C:/Users/Administrator/AppData/Roaming/Mozilla/Firefox/Profiles/10z1b5gf.default-release-1698134812236'
firefox_options = Options()
# firefox_options.add_argument("--headless")
firefox_options.profile = webdriver.FirefoxProfile(firefox_profile_directory)

firefox_options.headless = True
driver = webdriver.Firefox(options=firefox_options)
driver.get("https://temp-mail.org")
driver.session

print(driver.session_id)


aaa = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"main-wrapper\"]")))
print(aaa)


while(True):
    sleep(10)