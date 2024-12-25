from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from time import sleep
import quickstart_for_auto_open_profile
import requests
import keyboard

# BOT_TOKEN = "6582123842:AAEtweD7IPh-u62eCzqxrC1GfVgAySc7irg"
# CHAT_ID = 6416746860
BOT_TOKEN = "6597001968:AAG3SQh2eYDVY0vyeoXE9FtYfec3tJEr9qg"
CHAT_ID = 6330172738
 
def send_message(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    params = { "chat_id": CHAT_ID, "text": msg }
    requests.get(url, params=params)

def open_profile(email):
    url = "http://65.21.88.226:88/open-profile"
    payload = {
        "email": email
    }
    response = requests.post(url, json=payload)
    return response

while(True):
    quickstart_for_auto_open_profile.main()
    profilesEmail = quickstart_for_auto_open_profile.getProfilesEmail() 
    profilesStatus = quickstart_for_auto_open_profile.getProfileStatus()
    contactInfo = quickstart_for_auto_open_profile.getContactInfo()
    # print(profilesEmail)
    profilesEmail.pop(0)
    profilesStatus.pop(0)
    contactInfo.pop(0)
    print(len(profilesEmail))
    print(len(profilesStatus))
    print(len(contactInfo))
    # profilesEmail = ['samrat.fishel@my2ducks.com']

    index = 0
    # limit = int(len(profilesEmail) / 2)
    limit = int(len(profilesEmail))

    while (index < limit):
        
        if profilesStatus[index] == 'Available':
            try:
                driver = webdriver.Chrome()
                driver.maximize_window()

                email = profilesEmail[index]
                
                # email = "sailor.mung@my2ducks.com"
                password = "1234qwer!@#$"

                driver.get("https://www.upwork.com/ab/account-security/login")

                # sleep(5)
                # keyboard.press('tab')
                # keyboard.release('tab')
                sleep(1.5)
                # keyboard.press('space')  
                # keyboard.release('space')

                WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id=\"login_username\"]"))).send_keys(email)
                WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id=\"login_password_continue\"]"))).click()
                # WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id=\"login_username\"]"))).send_keys(PASSWORD)
                # keyboard.write(PASSWORD)
                WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[aria-label=\"Password\"]"))).send_keys(password)
                # keyboard.write(PASSWORD)
                WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id=\"login_control_continue\"]"))).click()

                # WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test=\"job-search-button\"]")))

                try:
                    WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"air3-alert-content\"]")))
                    alert_messages = driver.find_elements(By.CSS_SELECTOR, "div[class=\"air3-alert-content\"]")
                    for alert in alert_messages:
                        msg = alert.find_element(By.CSS_SELECTOR, ":first-child")
                        print(msg.text)
                        if "Action Required" in msg.text or "Action required" in msg.text:
                            RANGE_NAME = f'upwork profile!E{index + 2}:E'
                            quickstart_for_auto_open_profile.insertProfileStatus(RANGE_NAME, "Action Required")
                            pass
                        if "Suspended" in msg.text or "suspended" in msg.text:
                            RANGE_NAME = f'upwork profile!E{index + 2}:E'
                            quickstart_for_auto_open_profile.insertProfileStatus(RANGE_NAME, "Suspended")
                            pass
                        if "on hold" in msg.text:
                            RANGE_NAME = f'upwork profile!E{index + 2}:E'
                            quickstart_for_auto_open_profile.insertProfileStatus(RANGE_NAME, "on hold")
                            pass
                        
                except:
                    pass

                result_contact = False
                driver.get("https://www.upwork.com/ab/messages/rooms")
                
                try:
                    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[id=\"profile_person-profile-avatar\"]")))
                    print("Contact")
                    result_contact = True
                    send_message(f"Contact from {email}")
                    try:
                        open_profile(email)
                    except:
                        pass
                except:
                    print("No Contact")
                    pass
                
                if result_contact == True:
                    RANGE_NAME = f'upwork profile!D{index + 2}:D'
                    quickstart_for_auto_open_profile.insertContactInfo(RANGE_NAME, "Contact")
                else:
                    RANGE_NAME = f'upwork profile!D{index + 2}:D'
                    quickstart_for_auto_open_profile.insertContactInfo(RANGE_NAME, "No")
            except:
                pass
            index += 1
            driver.quit()
        else:
            index += 1
    sleep(3)