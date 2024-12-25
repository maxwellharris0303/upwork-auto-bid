from flask import Flask, request, jsonify
from flask_cors import CORS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from time import sleep

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

FILENAME = "contact_emails"
def email_save(email):
    with open(FILENAME, "a") as file:
        file.write(email + "\n")

@app.route('/open-profile', methods=['POST'])
def open_profile_bot():
    # print("hello")
    data = request.get_json()
    # print(data)
    email = data["email"]
    print(email)
    email_save(email)
    password = "1234qwer!@#$"

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.upwork.com/ab/account-security/login")

    sleep(1.5)
    WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id=\"login_username\"]"))).send_keys(email)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id=\"login_password_continue\"]"))).click()

    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[aria-label=\"Password\"]"))).send_keys(password)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id=\"login_control_continue\"]"))).click()
    sleep(5)
    driver.get("https://www.upwork.com/ab/messages/rooms")
    while(True):
        sleep(1000)
    return "True"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=88)