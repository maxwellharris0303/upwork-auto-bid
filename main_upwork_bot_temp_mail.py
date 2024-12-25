from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
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

def main(create_account_count):
    SKILL_SET = ["Full-stack Development", "Data Scraping", "Web Scraping", "Data Extraction", "Bot Development", "Automation", "Selenium", "Beautiful Soup", "Scrapy", "Python", "Browser Automation", "Google Sheets Automation", "Web Scraping Framework", "Automation Anywhere", "Marketing Automation"]

    OVERVIEW_TEXT = "Hello, I'm Assistant, a versatile and highly skilled professional with expertise in full-stack development, data scraping, web scraping, and bot development. With a strong background in Python and web scraping frameworks like Selenium, Beautiful Soup, and Scrapy, I'm capable of automating complex tasks and extracting valuable data from websites. Additionally, I specialize in browser automation and Google Sheets automation, utilizing my knowledge to streamline processes and enhance efficiency. Whether it's building AI bots or implementing marketing automation strategies, I bring a comprehensive skill set to deliver exceptional results."

    MY_TITLE = "Senior Full-stack Developer | Data Scraping, Automation Expert"
    MY_HOURLY_RATE = 35

    COUNTRY = 'Canada'

    # RESUME_PATH = "C:\\Auto Register\\resume\\1.pdf"
    # PHOTO_PATH = "C:\\Auto Register\\photo\\1.png"
    RESUME_PATH = f"{getPath.get_project_path()}\\resume\\1.pdf"
    PHOTO_PATH = f"{getPath.get_project_path()}\\photo\\{get_photo_directory_filenames.get_random_photo()}"

    BIRTH_OF_DATE = "1990-04-03"

    STREET_ADDRESS = "130 rue Levy"
    CITY_NAME = "Montreal"
    PHONE_NUMBER = "514-893-1337"
    ZIP_CODE = "H3C 5K4"

    FILENAME = 'email.txt'

    CREATE_INDEX = 1

    # CREATE_PROFILE_COUNT = input('Please input Profile Count to create: ')
    # CREATE_PROFILE_COUNT = int(CREATE_PROFILE_COUNT)
    CREATE_PROFILE_COUNT = create_account_count

    BID_TEMPLATE = ""
    BID_TEMPLATE_HEADER = "The client posted job like "
    # JOB_DESCRIPTION = "We are seeking a dedicated Social Media Manager to join our team at Woodez, an email marketing services company. Initially, your role will involve crafting engaging Instagram posts with a focus on showcasing our brand, including our adorable mascot, Woody the dog. You'll be responsible for creating captivating descriptions and managing the posting calendar."

    EXTRA_QUESTION_HEADER = "The client said me "
    EXTRA_QUESTION_TEMPLATE = ""

    BID_REQUEST = ""

    PASSWORD = "1234qwer!@#$"

    FILTERED_JOB_URL = "https://www.upwork.com/nx/search/jobs?amount=100-499,500-999,1000-4999,5000-&payment_verified=1&q=scraping&sort=recency&t=0,1"

    index_question = 0

    file_path = 'bidTemplate.txt'
    file_extra_question_path = 'extraQuestion.txt'
    firefox_profile_directory = 'C:/Users/Administrator/AppData/Roaming/Mozilla/Firefox/Profiles/li7rja6x.default-release'
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.profile = webdriver.FirefoxProfile(firefox_profile_directory)


    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            BID_TEMPLATE = contents
        with open(file_extra_question_path, 'r') as file1:
            contents1 = file1.read()
            EXTRA_QUESTION_TEMPLATE = contents1
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        print(f"File '{file_extra_question_path}' not found.")
    except IOError:
        print(f"An error occurred while reading the file '{file_path}'.")
        print(f"An error occurred while reading the file '{file_extra_question_path}'.")


    def bid_function(job_desc, extra_questions):
        response_chatgpt_array = []

        JOB_DESCRIPTION = job_desc
        BID_REQUEST = BID_TEMPLATE_HEADER + f"\"{JOB_DESCRIPTION}\"" + "\n" + BID_TEMPLATE

        extra_questions_count = len(extra_questions)
        index_question = 0


        firefox_driver = webdriver.Firefox(options=firefox_options)
        firefox_driver.maximize_window()
        firefox_driver.get("https://poe.com")

        input_chatgpt_text = WebDriverWait(firefox_driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea[class=\"GrowingTextArea_textArea__ZWQbP\"]")))
        input_chatgpt_text.send_keys(BID_REQUEST)

        WebDriverWait(firefox_driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"Button_buttonBase__Bv9Vx Button_primary__6UIn0 ChatMessageSendButton_sendButton__4ZyI4 ChatMessageInputContainer_sendButton__dBjTt\"]"))).click()

        WebDriverWait(firefox_driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"Button_buttonBase__Bv9Vx Button_tertiary__KEQm1 Button_iconOnly__poDNY\"]")))

        response_chatgpt = WebDriverWait(firefox_driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"Message_botMessageBubble__aYctV\"]:nth-child(1)")))
        response_chatgpt_result = response_chatgpt.find_element(By.CSS_SELECTOR, ":first-child")

        bid_final = BeautifulSoup(response_chatgpt_result.get_attribute("innerHTML"), 'html.parser').get_text()

        response_chatgpt_array.append(bid_final)

        if extra_questions_count == 0:
            firefox_driver.quit()
        else:
            while(index_question < extra_questions_count):
                EXTRA_QUESTION_REQUEST = EXTRA_QUESTION_HEADER + f"\"{extra_questions[index_question]}\"" + "\n" + EXTRA_QUESTION_TEMPLATE
                input_chatgpt_text = WebDriverWait(firefox_driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea[class=\"GrowingTextArea_textArea__ZWQbP\"]")))
                input_chatgpt_text.send_keys(EXTRA_QUESTION_REQUEST)

                WebDriverWait(firefox_driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"Button_buttonBase__Bv9Vx Button_primary__6UIn0 ChatMessageSendButton_sendButton__4ZyI4 ChatMessageInputContainer_sendButton__dBjTt\"]"))).click()
                WebDriverWait(firefox_driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"Button_buttonBase__Bv9Vx Button_tertiary__KEQm1 Button_iconOnly__poDNY\"]")))

                sleep(5)

                print(len(firefox_driver.find_elements(By.CLASS_NAME, 'Message_botMessageBubble__aYctV')))
                response_chatgpt = firefox_driver.find_elements(By.CLASS_NAME, 'Message_botMessageBubble__aYctV')[int(index_question) + 1]
                response_chatgpt_result = response_chatgpt.find_element(By.CSS_SELECTOR, ":first-child")

                extra_question_final = BeautifulSoup(response_chatgpt_result.get_attribute("innerHTML"), 'html.parser').get_text()
                print(extra_question_final)
                print("\n")

                response_chatgpt_array.append(extra_question_final)
                index_question += 1
            firefox_driver.quit()

        return response_chatgpt_array

    def parseProfile(profilePath):
        txt = open(profilePath).read().split('-' * 100 + '\n')

        essential = txt[0].split('\n')
        name = essential[0].split(' ')

        first_name = name[0]
        last_name = name[1]
        professional = essential[1]
        overview = essential[2]
        phone = essential[3].split(', ')[0]
        country = essential[3].split(', ')[1]
        hourRate = essential[4]
        workXP = [(
            i[0].replace('\n', '').split(', ')[0],
            i[0].replace('\n', '').split(', ')[1],
            i[1].replace('\n', '').split(', ')[0],
            i[1].replace('\n', '').split(', ')[1],
            i[2].replace('\n', '').split(' - ')[0],
            i[2].replace('\n', '').split(' - ')[1]
        ) for i in [j.split('\n') for j in txt[1].split('\n\n')]]

        education = [(
            i[0].replace('\n', ''),
            i[1].replace('\n', ''),
            i[2].replace('\n', ''),
            i[3].replace('\n', '').split(' - ')[0][:4],
            i[3].replace('\n', '').split(' - ')[1][:4]
        ) for i in [j.split('\n') for j in txt[2].split('\n\n')]]

        languages = [tuple(i.replace('\n', '').split(', ')) for i in txt[3].split('\n')][:-1]

        skills = [i for i in txt[4].split('\n')[0].replace('\n', '').split(', ')]
        services = [i for i in txt[4].split('\n')[1].replace('\n', '').split(', ')]

        last = txt[5].split('\n')
        street = last[0].replace('\n', '').split(', ')[0]
        zipcode = last[0].replace('\n', '').split(', ')[1]
        city = last[1].replace('\n', '').split(', ')[0]
        location = last[2]
        avatar = last[3]

        return {
            'first_name': first_name,
            'last_name': last_name,
            'professional': professional,
            'overview': overview,
            'country': country,
            'hourRate': hourRate,
            'workXP': workXP,
            'education': education,
            'languages': languages,
            'skills': skills,
            'services': services,
            'street': street,
            'zipcode': zipcode,
            'city': city,
            'location': location,
            'phone': phone,
            'avatar': avatar
        }

    global expFlag, photoDir
    expFlag = True
    photoDir = 'C:\\Users\\Administrator\\Pictures\\'

    curr_year = datetime.now().year

    # profile = input('file: ') #sys.argv[1]
    profile = 'Blaine King.txt' #sys.argv[1]
    hasResume = profile[-4:] == '.pdf'

    hasResume = True

    profile = parseProfile(profile)


    def waitInfinite(callback, debug = False):
        sleep(0.3)
        yet = True
        while yet:
            try:
                callback()
                yet = False
            except NoSuchElementException:
                print(1)
                pass
            except JavascriptException:
                print(2)
                pass
            except StaleElementReferenceException:
                print(3)
                pass

    def waitInfiniteEmailGetter(callback, debug = False):
        sleep(0.3)
        yet = 0
        while(yet < 50):
            try:
                callback()
                yet = 0
            except NoSuchElementException:
                yet += 1
                # print(1)
                pass
            except JavascriptException:
                yet += 1
                # print(2)
                pass
            except StaleElementReferenceException:
                yet += 1
                # print(3)
                pass
                
    def waitUntil(callback, driver, selector):
        sleep(0.3)
        yet = True
        while yet:
            try:
                callback(driver.find_element(By.CSS_SELECTOR, selector))
                yet = False
            except:
                pass

    def selectDropDownPeriod(dropdownId, itemSelector, period):
        driver.execute_script(f'document.querySelector(\'div[class="{dropdownId}"]\').click()')
        sleep(0.5)
        nations = driver.find_elements(By.CSS_SELECTOR, itemSelector)

        if str(type(period)) == "<class 'int'>":
            driver.execute_script(f'document.querySelectorAll("{itemSelector}")[{str(period)}].click()')
        else:
            for i in range(len(nations)):
                try:
                    if nations[i].text.find(period) >= 0:
                        driver.execute_script(f'document.querySelectorAll("{itemSelector}")[{str(i)}].click()')
                        break
                except:
                    pass

    def extract_strings(array):
        start_index = array.index("Cover Letter")
        end_index = array.index("Attachments")
        extracted_strings = array[start_index + 1:end_index]
        return extracted_strings

    def email_save(email):
        with open(FILENAME, "a") as file:
            file.write(email + "\n")

        quickstart.main()
        quickstart.getProfileData()
        columnCount = quickstart.getColumnCount()
        print(f'Number of Profiles: {columnCount}')

        insert_profile = columnCount + 1

        quickstart.insertData(f'upwork profile!A{insert_profile}:A', email, f'upwork profile!B{insert_profile}:B')


    while(CREATE_INDEX <= CREATE_PROFILE_COUNT):
        try:
            firefox_email_options = webdriver.FirefoxOptions()
            firefox_email_options.add_argument("--headless")
            firefox_email_options.profile = webdriver.FirefoxProfile(firefox_profile_directory)
            emailGetter = webdriver.Firefox(options=firefox_email_options)

            #Get Temp URL

            emailGetter.get("https://temp-mail.org/")
            delete_button = WebDriverWait(emailGetter, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"no-ajaxy tm-btn btn-gray click-to-delete\"]")))
            emailGetter.execute_script("arguments[0].click();", delete_button)
            # delete_button.click()

            WebDriverWait(emailGetter, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"btn-rds icon-btn bg-theme click-to-copy copyIconGreenBtn\"]")))
            # copy_button.click()
            input_box = WebDriverWait(emailGetter, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[class=\"emailbox-input opentip\"]")))
            # print(input_box.get_attribute('value'))

            tempURL = input_box.get_attribute('value')

            

            #Sign up

            # options = webdriver.ChromeOptions()
            # options.add_argument("--headless")

            # driver = webdriver.Chrome(options=options)
            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.get("https://www.upwork.com/nx/signup/?dest=home")
            sleep(5)
            keyboard.press('tab')
            keyboard.release('tab')
            sleep(1.5)
            keyboard.press('space')
            keyboard.release('space')

            
            # driver = webdriver.Firefox()
            # driver.maximize_window()

            # driver.get("https://www.upwork.com/ab/account-security/login")
            # WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[class=\"up-n-link air3-btn air3-btn-secondary width-sm btn-block-sm mt-3x mb-6x px-8x\"]"))).click()
            
            # driver.get("https://www.upwork.com/nx/signup/?dest=home")
            first_name, last_name = random_name_generator.random_name('male')

            if first_name.endswith('.'):
                first_name, last_name = random_name_generator.random_name('male')

            # sleep(10)

            WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[id=\"button-box-4\"]"))).click()
            driver.find_element(By.CSS_SELECTOR, "button[data-qa='btn-apply']").click()


            # driver.find_element(By.ID, "first-name-input").send_keys(profile['first_name'])
            # driver.find_element(By.ID, "last-name-input").send_keys(profile['last_name'])
            driver.find_element(By.ID, "first-name-input").send_keys(first_name)
            driver.find_element(By.ID, "last-name-input").send_keys(last_name)
            driver.find_element(By.ID, "redesigned-input-email").send_keys(tempURL)
            driver.find_element(By.ID, "password-input").send_keys(PASSWORD)

            def clickByMouse(element):
                ActionChains(driver).click(element)\
                                    .perform()

            def selectDropDown(dropdownId, itemSelector, country):
                driver.execute_script(f'document.querySelector(\'#{dropdownId}\').click()')
                sleep(0.5)
                nations = driver.find_elements(By.CSS_SELECTOR, itemSelector)

                if str(type(country)) == "<class 'int'>":
                    driver.execute_script(f'document.querySelectorAll("{itemSelector}")[{str(country)}].click()')
                else:
                    for i in range(len(nations)):
                        try:
                            if nations[i].text.find(country) >= 0:
                                driver.execute_script(f'document.querySelectorAll("{itemSelector}")[{str(i)}].click()')
                                break
                        except:
                            pass

            def selectDateDropDown(dropdownId, itemSelector, country):
                tmp = dropdownId.split('##')
                if len(tmp) == 2:
                    dropdownId = tmp[0]
                    driver.execute_script(f'document.querySelectorAll(\'div[aria-labelledby^="{dropdownId}"]\')[{tmp[1]}].click()')
                else:
                    driver.execute_script(f'document.querySelector(\'div[aria-labelledby^="{dropdownId}"]\').click()')
                sleep(0.5)
                nations = driver.find_elements(By.CSS_SELECTOR, itemSelector)

                if str(type(country)) == "<class 'int'>":
                    driver.execute_script(f'document.querySelectorAll("{itemSelector}")[{str(country)}].click()')
                else:
                    for i in range(len(nations)):
                        try:
                            if nations[i].text.find(country) >= 0:
                                driver.execute_script(f'document.querySelectorAll("{itemSelector}")[{str(i)}].click()')
                                break
                        except:
                            pass

            sleep(1)
            selectDropDown("dropdown-label-7", "li.up-menu-item", COUNTRY)
            driver.execute_script('document.querySelectorAll("span.up-checkbox-replacement-helper")[1].click()')
            sleep(1)
            driver.execute_script('document.getElementById("button-submit-form").click()')
            sleep(9)
            def verifyEmail():
                inbox_verify = emailGetter.find_element(By.LINK_TEXT, "Verify your email address")
                # inbox_verify.click()
                emailGetter.execute_script("arguments[0].click();", inbox_verify)
                
            waitInfiniteEmailGetter(verifyEmail)
            sleep(8)
            print("HAHA")
            verified_element = emailGetter.find_element(By.LINK_TEXT, "Verify Email")
            print("DFSDFF")
            verifiedURL = verified_element.get_attribute('href')
            print("sdfsdf")
            print(verifiedURL)
            
            try:
                emailGetter.quit()
            except:
                try:
                    emailGetter.close()
                except:
                    pass
            # driver.quit()
            driver.get(verifiedURL)

            # driver = webdriver.Chrome()
            # driver.maximize_window()
            # driver.get(verifiedURL)
            # sleep(5)
            # keyboard.press('tab')
            # keyboard.release('tab')
            # sleep(1.5)
            # keyboard.press('space')
            # keyboard.release('space')

            # WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id=\"login_username\"]"))).send_keys(tempURL)
            # WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id=\"login_password_continue\"]"))).click()

            # WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[aria-label=\"Password\"]"))).send_keys(PASSWORD)
            # WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id=\"login_control_continue\"]"))).click()

            try:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"air3-btn air3-btn-primary mr-7\"]"))).click()
            except:
                WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[class=\"up-n-link nav-brand nav-d-flex\"]"))).click()
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"air3-btn air3-btn-primary mr-7\"]"))).click()

            WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test=\"skip-button\"]"))).click()
            WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test=\"skip-button\"]"))).click()
            WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test=\"skip-button\"]"))).click()

            sleep(2)

                

            def addLanguage(driver, language, pro, count):
                pro = eval(pro)
                driver.execute_script('document.querySelector("button.air3-btn.air3-btn-secondary.air3-btn-sm").click()')
                
                waitInfinite(lambda: selectDateDropDown(f"dropdown-label-language-{count}", "span.air3-menu-item-text", language))
                waitInfinite(lambda: selectDateDropDown(f"dropdown-label-proficiency-{count}", "span.air3-menu-item-text", pro))

                return count + 1

            def addSkill(driver, inp, skill, field = "skills-input"):
                
                waitUntil(lambda x: x.click(), driver, f'input[aria-labelledby="{field}"]')
                waitUntil(lambda x: x.send_keys(skill), driver, f'input[aria-labelledby="{field}"]')
                
                flag = True
                while flag:
                    nations = driver.find_elements(By.CSS_SELECTOR, "span.air3-menu-item-text")
                    flag = len(nations) == 0

                for i in range(len(nations)):
                    try:
                        if nations[i].text.find(skill) >= 0:
                            driver.execute_script(f'document.querySelectorAll("span.air3-menu-item-text")[{str(i)}].click()')
                            break
                    except:
                        pass
                    
                sleep(0.5)

            def addService(driver, services):
                waitUntil(lambda x: x.click(), driver, 'div[data-test="dropdown-toggle"]')
                sleep(1)

                for service in services:
                    driver.execute_script(f'''
                        // document.querySelector(\'div[data-test="dropdown-toggle"]\').click()
                        var services = document.querySelectorAll('span.air3-menu-checkbox-labels');
                        var toselect;
                        for (let i = 0; i < services.length; i++) {{
                            console.log(services[i], '{service}');
                            if (services[i].textContent.indexOf('{service}') >= 0) {{
                                toselect = services[i].parentNode.parentNode;
                                break;
                            }}
                        }}
                        if (toselect) {{
                            if (toselect.getAttribute("aria-selected") == 'false') {{
                                toselect.parentNode.parentNode.parentNode.click();
                                setTimeout(() => toselect.click(), 300);
                            }}
                        }}
                    ''')
                    sleep(0.1)

            def configLast(driver, country, street, city, zipcode, phone, photo):
                global photoDir
                selectDateDropDown("country-label", "span.air3-menu-item-text", country)
                waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby="street-label"]').send_keys(street))
                
                addSkill(driver, driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby="city-label"]'), city, "city-label")

                waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby="postal-code-label"]').send_keys(zipcode))
                waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby^="dropdown-label-phone-number"]').send_keys(phone))

                waitInfinite(lambda: driver.execute_script("document.querySelector('button[data-cy=\"open-loader\"]').click()"))
                sleep(1)

                waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(photoDir + photo))
                waitInfinite(lambda: driver.execute_script("document.querySelectorAll('button.air3-btn.air3-btn-primary')[1].click()"))

            if hasResume:
                WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa=\"resume-upload-btn-mobile\"]"))).click()

                parent_file_selector = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span[class=\"fe-upload-btn upload-btn\"]')))
                child_file_selector = parent_file_selector.find_element(By.CSS_SELECTOR, ":nth-child(2)")
                child_file_selector.send_keys(RESUME_PATH)

                continueButtonText = ""
                continueButton = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa=\"resume-upload-continue-btn\"]")))

                while(continueButtonText != "Continue"):
                    continueButtonText = continueButton.text

                continueButton.click()

                titleInput = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[aria-labelledby=\"title-label\"]")))
                titleInput.clear()
                titleInput.send_keys(MY_TITLE)

                WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test=\"next-button\"]"))).click()
                WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test=\"next-button\"]"))).click()
                WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test=\"next-button\"]"))).click()

                selectDropDownPeriod("air3-dropdown-icon air3-icon md", "li.air3-menu-item", "Native or Bilingual")
                WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test=\"next-button\"]"))).click()


                WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[aria-labelledby=\"skills-input\"]")))

                def input_skills(skill, driv):
                    skillsInput = (By.CSS_SELECTOR, "input[aria-labelledby=\"skills-input\"]")
                    skill_element = WebDriverWait(driv, 10).until(EC.presence_of_element_located(skillsInput))
                    index = False
                    while(index == False):
                        try:
                            skill_element = WebDriverWait(driv, 10).until(EC.presence_of_element_located(skillsInput))
                            skill_element.click()
                            skill_element.clear()
                            skill_element.send_keys(skill)
                            skill_dropdown = WebDriverWait(driv, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul[class=\"air3-menu-list\"]")))
                            skill_dropdown.find_element(By.CSS_SELECTOR, ":first-child").click()
                            index = True
                            print("1")
                        except StaleElementReferenceException:
                            # If the element becomes stale, re-locate it and try again
                            skill_element = WebDriverWait(driv, 10).until(EC.presence_of_element_located(skillsInput))
                            skill_element.click()
                            skill_element.clear()
                            skill_element.send_keys(skill)
                            skill_dropdown = WebDriverWait(driv, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul[class=\"air3-menu-list\"]")))
                            skill_dropdown.find_element(By.CSS_SELECTOR, ":first-child").click()
                            index = True
                            print("2")

                for skill in SKILL_SET:
                    input_skills(skill, driver)

                    

                WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test=\"next-button\"]"))).click()

                textArea_Overview = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea[aria-labelledby=\"overview-label\"]")))
                textArea_Overview.clear()
                textArea_Overview.send_keys(OVERVIEW_TEXT)

                WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test=\"next-button\"]"))).click()

                WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa=\"category-add-btn\"]")))
                service_offers = driver.find_elements(By.CSS_SELECTOR, "button[data-qa=\"category-add-btn\"]")
                for offer in service_offers:
                    offer.click()

                WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test=\"next-button\"]"))).click()

                hourly_rate_input = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder=\"$0.00\"]")))
                hourly_rate_input.send_keys(MY_HOURLY_RATE)

                WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test=\"next-button\"]"))).click()

                try:
                    upload_photo_button = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa=\"open-loader\"]")))
                    upload_photo_button.click()

                    parent_input = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"air3-image-crop-input-container is-empty\"]")))

                    input_photo = parent_input.find_element(By.TAG_NAME, "input")
                    input_photo.send_keys(PHOTO_PATH)

                    save_button = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa=\"btn-save\"]")))
                    save_button.click()

                    sleep(10)
                    # WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"air3-image-crop-area\"]")))
                    
                    birthday_input = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[aria-labelledby=\"date-of-birth-label\"]")))
                    # while(birthday_input.is_displayed() and birthday_input.is_enabled()):
                    #     sleep(1)
                    #     print("not")
                    birthday_input.send_keys(BIRTH_OF_DATE)
                    WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[aria-labelledby=\"street-label\"]"))).send_keys(STREET_ADDRESS)

                    city_name_input = (By.CSS_SELECTOR, "input[aria-labelledby=\"city-label\"]")
                    city_name_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(city_name_input))

                    index = False
                    while(index == False):
                        try:
                            city_name_element.click()
                            city_name_element.clear()
                            city_name_element.send_keys(CITY_NAME)
                            cityname_dropdown = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul[aria-labelledby=\"city-label\"]")))
                            cityname_dropdown.find_element(By.CSS_SELECTOR, ":first-child").click()
                            index = True
                            print("3")
                        except StaleElementReferenceException:
                            # If the element becomes stale, re-locate it and try again
                            city_name_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(city_name_input))
                            city_name_element.click()
                            city_name_element.clear()
                            city_name_element.send_keys(CITY_NAME)
                            cityname_dropdown = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul[aria-labelledby=\"city-label\"]")))
                            cityname_dropdown.find_element(By.CSS_SELECTOR, ":first-child").click()
                            index = True
                            print("4")

                    WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[aria-labelledby=\"postal-code-label\"]"))).send_keys(ZIP_CODE)
                    WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[inputmode=\"numeric\"]"))).send_keys(PHONE_NUMBER)
                    

                    WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test=\"next-button\"]"))).click()

                    WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa=\"submit-profile-top-btn\"]"))).click()
                except:
                    pass

                email_save(tempURL)


                sleep(3)

                # driver.get("https://www.upwork.com/nx/jobs/search/?q=web%20OR%20wordpress%20OR%20shopify%20OR%20ecommerce%20OR%20woocommerce%20OR%20wix%20OR%20webflow&sort=recency&t=0,1&amount=100-499,500-999,1000-4999,5000-&payment_verified=1")
                driver.get(FILTERED_JOB_URL)

                # WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h2[class=\"my-0 p-sm-right job-tile-title\"]"))).click()
                sleep(5)
                try:
                    driver.execute_script(f'document.querySelectorAll(\'h2[class="my-0 p-sm-right job-tile-title"]\')[0].click()')
                    sleep(3)
                    move_to_apply_url = driver.find_elements(By.TAG_NAME, 'h2')[1]

                    job_desc = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"job-description break mb-0\"]")))
                    job_desc_text = job_desc.find_element(By.CSS_SELECTOR, ":first-child").text
                    print(job_desc_text)
                    print("\n")

                    url = move_to_apply_url.find_element(By.CSS_SELECTOR, ":first-child").get_attribute('href')
                    print(url)
                    driver.get(url)
                except:
                    driver.execute_script(f'document.querySelectorAll(\'h2[class="h4 mb-0 mr-2"]\')[0].click()')
                    open_new_window = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-test=\"slider-open-in-new-window UpLink\"]")))
                    new_url = open_new_window.get_attribute('href')

                    base_url = "https://www.upwork.com/"

                    move_to_apply_url = urljoin(base_url, new_url)

                    job_desc = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"break mt-10\"]")))
                    job_desc_text = job_desc.find_element(By.CSS_SELECTOR, ":first-child").text
                    print(job_desc_text)
                    print("\n")

                    driver.get(move_to_apply_url)

                WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label=\"Apply Now\"]"))).click()

                close_button = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"up-btn mt-0 mb-0 up-btn-primary\"]")))
                close_button.click()

                def hourly_or_fixed():
                    try:
                        WebDriverWait(driver, 6).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id=\"step-rate\"]")))
                        return "hourly"
                    except:
                        return "fixed"
                    
                job_type = hourly_or_fixed()
                if(job_type == "hourly"):
                    print("hour")
                    try:
                        selectDropDownPeriod("up-dropdown-icon up-icon", "li.up-menu-item", "Never")
                        sleep(1)
                        driver.execute_script(f'document.querySelectorAll(\'div[class="text-muted mt-5"]\')[1].click()')
                    except:
                        pass
                if(job_type == "fixed"):
                    print("fix")
                    try:
                        selectDropDownPeriod("up-dropdown-icon up-icon", "li.up-menu-item", "Less than 1 month")
                        sleep(1)
                        driver.execute_script(f'document.querySelectorAll(\'div[class="text-muted mt-5"]\')[1].click()')
                    except:
                        pass


                textarea_count = len(driver.find_elements(By.TAG_NAME, 'textarea'))
                # print(textarea_count)

                array_extra_questions = []

                textarea_label = driver.find_elements(By.CSS_SELECTOR, 'label.up-label')
                for i in textarea_label:
                    array_extra_questions.append(i.text)
                    
                # print(array_extra_questions)

                def extract_strings(array):
                    start_index = array.index("Cover Letter")
                    end_index = array.index("Attachments")
                    extracted_strings = array[start_index + 1:end_index]
                    return extracted_strings
                
                new_array_extra_questions = extract_strings(array_extra_questions)
                print(new_array_extra_questions)

                response_chatgpt_array = bid_function(job_desc_text, new_array_extra_questions)
                print(response_chatgpt_array[0])

                # cover_letter_textarea = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea[aria-labelledby=\"cover_letter_label\"]")))
                # cover_letter_textarea.send_keys(response_chatgpt_array[0])

                textarea_elements = driver.find_elements(By.TAG_NAME, 'textarea')
                index_textarea = 0
                while(index_textarea < textarea_count):
                    textarea_elements[index_textarea].send_keys(response_chatgpt_array[index_textarea])
                    index_textarea += 1

                

                bid_amount = 0
                try:
                    boost_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-ev-label=\"boost_set_bid_amount\"]")))
                    if boost_button.get_attribute('disabled') != "disabled":
                        boost_button.click()
                        boost_bid_amount = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id=\"boost-bid-amount\"]")))
                        boost_bid_amount.clear()
                        boost_bid_amount.send_keys("50")
                        WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-ev-label=\"boost_add_or_edit_bid\"]"))).click()
                        bid_amount = 50
                        send_proposal_button = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"up-btn up-btn-primary m-0\"]")))
                        send_proposal_button.click()
                except:
                    pass
                
                if bid_amount != 50:
                    send_proposal_button = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"up-btn up-btn-primary m-0\"]")))
                    send_proposal_button.click()
                    numbers = re.findall(r'\d+', send_proposal_button.text)
                    numbers = [int(num) for num in numbers]
                    print(numbers)
                    bid_amount = numbers[0]

                try:
                    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"checkbox\"]"))).click()
                    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"up-btn up-btn-primary m-0 btn-primary\"]"))).click()
                    sleep(2)
                    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"checkbox\"]"))).click()
                    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"up-btn up-btn-primary m-0 btn-primary\"]"))).click()
                except:
                    pass

                sleep(3)

                quickstart.main()
                quickstart.getProfileData()
                columnCount1 = quickstart.getColumnCount()
                # start_index_to_insert_bid_status = columnCount + 1
                quickstart.insertBidStatusData(f'upwork profile!C{columnCount1}:C', bid_amount)

                driver.quit()
                sleep(10)
                CREATE_INDEX += 1
            else:
                print("Error")
        except:
            try:
                driver.quit()
            except Exception as e:
                print("Error: " + {e})
                driver.quit()
                pass
    return tempURL, first_name, last_name, bid_amount