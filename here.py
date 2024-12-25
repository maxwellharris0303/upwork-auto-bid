from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import ui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import *
from time import sleep
from datetime import datetime
import sys
import keyboard
from bs4 import BeautifulSoup

SKILL_SET = ["Front-End Development", "Angular", "Vue.js", "Back-End Development", "Laravel", "Firebase Cloud Firestore", "Tailwind CSS", "HTML5", "CSS 3", "Google APIs"]

OVERVIEW_TEXT = "Hi there! I'm a versatile developer with expertise in CMS development, including WordPress, Shopify, and Wix. I also excel in e-commerce solutions like WooCommerce and have a knack for creating stunning online stores. Additionally, I have experience in mobile app development and can build engaging applications for both iOS and Android platforms. With my skills in bot development and Selenium, I can automate tasks and streamline processes, making your life easier. Let's collaborate to bring your digital ideas to life!"

MY_HOURLY_RATE = 35

RESUME_PATH = "C:\\Users\\Administrator\\Downloads\\100%.pdf"
PHOTO_PATH = "C:\\Users\\Administrator\\Documents\\111\\444.png"

BIRTH_OF_DATE = "1992-03-03"

STREET_ADDRESS = "Brandenburgische Strasse 72"
CITY_NAME = "Schweighofen"
PHONE_NUMBER = "06342149674"
ZIP_CODE = "76889"

FILENAME = 'email.txt'

CREATE_INDEX = 1

CREATE_PROFILE_COUNT = input('Please input Profile Count to create: ')
CREATE_PROFILE_COUNT = int(CREATE_PROFILE_COUNT)

BID_TEMPLATE = ""
BID_TEMPLATE_HEADER = "The client posted job like "
JOB_DESCRIPTION = "We are seeking a dedicated Social Media Manager to join our team at Woodez, an email marketing services company. Initially, your role will involve crafting engaging Instagram posts with a focus on showcasing our brand, including our adorable mascot, Woody the dog. You'll be responsible for creating captivating descriptions and managing the posting calendar."

EXTRA_QUESTION_HEADER = "The client said me "
EXTRA_QUESTION_TEMPLATE = ""

BID_REQUEST = ""

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

    input_chatgpt_text = WebDriverWait(firefox_driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea[class=\"GrowingTextArea_textArea__ZWQbP\"]")))
    input_chatgpt_text.send_keys(BID_REQUEST)

    WebDriverWait(firefox_driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"Button_buttonBase__Bv9Vx Button_primary__6UIn0 ChatMessageSendButton_sendButton__4ZyI4 ChatMessageInputContainer_sendButton__dBjTt\"]"))).click()

    WebDriverWait(firefox_driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"Button_buttonBase__Bv9Vx Button_tertiary__KEQm1 Button_iconOnly__poDNY\"]")))

    response_chatgpt = WebDriverWait(firefox_driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"Message_botMessageBubble__aYctV\"]:nth-child(1)")))
    response_chatgpt_result = response_chatgpt.find_element(By.CSS_SELECTOR, ":first-child")

    bid_final = BeautifulSoup(response_chatgpt_result.get_attribute("innerHTML"), 'html.parser').get_text()

    response_chatgpt_array.append(bid_final)

    if extra_questions_count == 0:
        firefox_driver.quit()
    else:
        while(index_question < extra_questions_count):
            EXTRA_QUESTION_REQUEST = EXTRA_QUESTION_HEADER + f"\"{extra_questions[index_question]}\"" + "\n" + EXTRA_QUESTION_TEMPLATE
            input_chatgpt_text = WebDriverWait(firefox_driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea[class=\"GrowingTextArea_textArea__ZWQbP\"]")))
            input_chatgpt_text.send_keys(EXTRA_QUESTION_REQUEST)

            WebDriverWait(firefox_driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"Button_buttonBase__Bv9Vx Button_primary__6UIn0 ChatMessageSendButton_sendButton__4ZyI4 ChatMessageInputContainer_sendButton__dBjTt\"]"))).click()
            WebDriverWait(firefox_driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"Button_buttonBase__Bv9Vx Button_tertiary__KEQm1 Button_iconOnly__poDNY\"]")))

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

profile = input('file: ') #sys.argv[1]
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

while(CREATE_INDEX <= CREATE_PROFILE_COUNT):

    emailGetter = webdriver.Chrome()

    #Get Temp URL

    emailGetter.get("https://www.minuteinbox.com/")
    tempURL = WebDriverWait(emailGetter, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[id=\"email\"]"))).text

    def email_save(email):
        with open(FILENAME, "a") as file:
            file.write(email + "\n")

    print(tempURL)

    #Sign up

    # options = webdriver.ChromeOptions()
    # options.add_argument("--headless")

    # driver = webdriver.Chrome(options=options)

    driver = webdriver.Chrome()
    driver.maximize_window()

    # driver.get("https://www.upwork.com/ab/account-security/login")
    # WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[class=\"up-n-link air3-btn air3-btn-secondary width-sm btn-block-sm mt-3x mb-6x px-8x\"]"))).click()
    
    driver.get("https://www.upwork.com/nx/signup/?dest=home")
    sleep(5)
    keyboard.press('tab')
    keyboard.release('tab')
    sleep(1.5)
    keyboard.press('space')
    keyboard.release('space')

    # sleep(10)

    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[id=\"button-box-4\"]"))).click()
    driver.find_element(By.CSS_SELECTOR, "button[data-qa='btn-apply']").click()


    driver.find_element(By.ID, "first-name-input").send_keys(profile['first_name'])
    driver.find_element(By.ID, "last-name-input").send_keys(profile['last_name'])
    driver.find_element(By.ID, "redesigned-input-email").send_keys(tempURL)
    driver.find_element(By.ID, "password-input").send_keys("1234qwer!@#$")

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
    selectDropDown("dropdown-label-7", "li.up-menu-item", profile['country'])
    driver.execute_script('document.querySelectorAll("span.up-checkbox-replacement-helper")[1].click()')
    sleep(1)
    driver.execute_script('document.getElementById("button-submit-form").click()')
    sleep(9)
    def verifyEmail():
        emailGetter.execute_script('x = document.querySelectorAll("td.from")[0];if(x.textContent == " Upwork Notifications ") x.click()')
        sleep(4)
        iframe = emailGetter.find_element(By.ID, "iframeMail")
        emailGetter.switch_to.frame(iframe)

    waitInfinite(verifyEmail)
    verifiedURL = emailGetter.find_elements(By.TAG_NAME, 'a')[1].get_attribute('href')

    try:
        emailGetter.quit()
    except:
        try:
            emailGetter.close()
        except:
            pass
        

    driver.get(verifiedURL)

    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"air3-btn air3-btn-primary mr-7\"]"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test=\"skip-button\"]"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test=\"skip-button\"]"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test=\"skip-button\"]"))).click()
    # driver.execute_script('document.querySelector("button.air3-btn.air3-btn-primary.mr-7").click()')
    # sleep(2)
    # driver.execute_script('document.querySelector(\'button[data-test="skip-button"]\').click()')
    # sleep(2)
    # driver.execute_script('document.querySelector(\'button[data-test="skip-button"]\').click()')
    # sleep(2)
    # driver.execute_script('document.querySelector(\'button[data-test="skip-button"]\').click()')
    sleep(2)

    # driver.execute_script('document.querySelector(\'button[data-qa="resume-upload-btn-mobile"]\').click()')
    # waitInfinite(lambda: driver.execute_script('document.querySelector(\'button[data-qa="resume-upload-btn-mobile"]\').click()'))

    def addExperience(driver, title, comapny, city, country, start, end = 'current'):
        global expFlag
        if expFlag:
            waitInfinite(lambda: driver.execute_script('document.querySelector("button.air3-btn.air3-btn-lg.air3-btn-secondary-inverted.air3-btn-circle").click()'))
        else:
            waitInfinite(lambda: driver.execute_script('document.querySelector("button.air3-btn.air3-btn-secondary.air3-btn-circle").click()'))


        if expFlag: waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Ex: Software Engineer"]').send_keys(""))
        waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Ex: Software Engineer"]').send_keys(title))
        sleep(1)
        waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Ex: Microsoft"]').send_keys(comapny))
        sleep(1)
        waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Ex: London"]').send_keys(city))
        waitInfinite(lambda: selectDateDropDown("location-label", "span.air3-menu-item-text", country))


        start_year = eval(start.split('.')[0])
        start_month = eval(start.split('.')[1])
        waitInfinite(lambda: selectDateDropDown("start-date-month", "span.air3-menu-item-text", start_month - 1))
        waitInfinite(lambda: selectDateDropDown("start-date-year", "span.air3-menu-item-text", curr_year - start_year))

        if end == 'current':
            driver.execute_script('document.querySelector(\'span[data-test="checkbox-input"]\').click()')
        else:
            end_year = eval(end.split('.')[0])
            end_month = eval(end.split('.')[1])
            waitInfinite(lambda: selectDateDropDown("end-date-month", "span.air3-menu-item-text", end_month - 1))
            waitInfinite(lambda: selectDateDropDown("end-date-year", "span.air3-menu-item-text", curr_year - end_year))
            
        driver.execute_script('document.querySelector(\'button[data-qa="btn-save"]\').click()')

        print("QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ")

        expFlag = False
        
    def addEducation(driver, school, degree, field, start, end):
        start = eval(start)
        end = eval(end)
        global expFlag
        if expFlag:
            print("111111111QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ")
            waitInfinite(lambda: driver.execute_script('document.querySelector("button.air3-btn.air3-btn-circle").click()'))   
            sleep(9)
            driver.execute_script('document.querySelector(\'button[data-test="close-button"]\').click()')
        else:
            print("22222222222QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ")
            waitInfinite(lambda: driver.execute_script('document.querySelector("button.air3-btn.air3-btn-secondary.air3-btn-circle").click()'))

        sleep(3)
        waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Ex: Northwestern University"]').send_keys(school))
        print("33333333QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ")
        waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby="degree-label"]').send_keys(""))
        if degree != '###': waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby="degree-label"]').send_keys(degree))
        print("4444444444444QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ")
        waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby="area-of-study-label"]').send_keys(""))
        waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby="area-of-study-label"]').send_keys(field))

        print("55555555555QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ")
        waitInfinite(lambda: selectDateDropDown("dates-attended-label##0", "span.air3-menu-item-text", curr_year - start + 1))
        waitInfinite(lambda: selectDateDropDown("dates-attended-label##1", "span.air3-menu-item-text", 2030 - end + 1))
        driver.execute_script('document.querySelector(\'button[data-test="save-btn"]\').click()')
        print("22222222222QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ")
        expFlag = False

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
        WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa=\"resume-upload-btn-mobile\"]"))).click()
        WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[class=\"up-n-link\"]"))).click()

        # file_selector = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"file\"]"))).click()
        # file_selector.send_keys("C:/Users/Administrator/Pictures/resume.pdf")
        sleep(1)
        keyboard.write(RESUME_PATH)
        keyboard.press('tab')
        keyboard.release('tab')
        keyboard.press('tab')
        keyboard.release('tab')
        keyboard.press('enter')
        keyboard.release('enter')

        continueButtonText = ""
        continueButton = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa=\"resume-upload-continue-btn\"]")))

        while(continueButtonText != "Continue"):
            continueButtonText = continueButton.text

        continueButton.click()

        titleInput = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[aria-labelledby=\"title-label\"]")))
        titleInput.clear()
        titleInput.send_keys("Senior Full-stack Developer | Wordpress, Shopify Expert")

        WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test=\"next-button\"]"))).click()
        WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test=\"next-button\"]"))).click()
        WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test=\"next-button\"]"))).click()
        WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test=\"next-button\"]"))).click()

        

        def input_skills(skill):
            skillsInput = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[aria-labelledby=\"skills-input\"]")))
            skillsInput.send_keys(skill)
            sleep(0.8)
            keyboard.press('tab')
            keyboard.release('tab')
            keyboard.press('tab')
            keyboard.release('tab')
            keyboard.press('enter')        
            keyboard.release('enter')

        skill_set_length = len(SKILL_SET)

        for skill in SKILL_SET:
            input_skills(skill)

        WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test=\"next-button\"]"))).click()

        textArea_Overview = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea[aria-labelledby=\"overview-label\"]")))
        textArea_Overview.clear()
        textArea_Overview.send_keys(OVERVIEW_TEXT)

        WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test=\"next-button\"]"))).click()
        sleep(1)
        service_offers = driver.find_elements(By.CSS_SELECTOR, '[data-qa="category-add-btn"]')
        service_offers_length = len(service_offers)
        print(service_offers_length)

        INDEX_OFFER = 1

        keyboard.press('tab')
        keyboard.release('tab')

        while(INDEX_OFFER <= service_offers_length):
            keyboard.press('tab')
            keyboard.release('tab')
            keyboard.press('enter')        
            keyboard.release('enter')
            INDEX_OFFER = INDEX_OFFER + 1

        WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test=\"next-button\"]"))).click()

        hourly_rate_input = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder=\"$0.00\"]")))
        hourly_rate_input.send_keys(MY_HOURLY_RATE)

        WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test=\"next-button\"]"))).click()

        try:

            upload_photo_button = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label=\"Upload photo\"]")))
            upload_photo_button.click()

            sleep(1)
            keyboard.press('tab')
            keyboard.release('tab')
            keyboard.press('tab')
            keyboard.release('tab')
            keyboard.press('enter')
            keyboard.release('enter')

            # WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id=\"image-crop-17\"]"))).click()

            sleep(1)
            keyboard.write(PHOTO_PATH)
            keyboard.press('tab')
            keyboard.release('tab')
            keyboard.press('tab')
            keyboard.release('tab')
            keyboard.press('enter')
            keyboard.release('enter')
            sleep(1)
            keyboard.press('tab')
            keyboard.release('tab')
            keyboard.press('tab')
            keyboard.release('tab')
            keyboard.press('tab')
            keyboard.release('tab')
            keyboard.press('tab')
            keyboard.release('tab')
            keyboard.press('tab')
            keyboard.release('tab')
            keyboard.press('tab')
            keyboard.release('tab')
            keyboard.press('enter')
            keyboard.release('enter')

            sleep(5)

            birthday_input = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[aria-labelledby=\"date-of-birth-label\"]")))
            # while(birthday_input.is_displayed() and birthday_input.is_enabled()):
            #     sleep(1)
            #     print("not")
            birthday_input.send_keys(BIRTH_OF_DATE)
            WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[aria-labelledby=\"street-label\"]"))).send_keys(STREET_ADDRESS)

            # WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[class=\"air3-typeahead-input-main air3-input\"]"))).send_keys(CITY_NAME)

            keyboard.press('tab')
            keyboard.release('tab')
            keyboard.press('tab')
            keyboard.release('tab')
            keyboard.write(CITY_NAME)
            
            
            sleep(2)
            keyboard.press('tab')
            keyboard.release('tab')
            keyboard.press('tab')
            keyboard.release('tab')
            keyboard.press('enter')
            keyboard.release('enter')

            WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[aria-labelledby=\"postal-code-label\"]"))).send_keys(ZIP_CODE)
            WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[inputmode=\"numeric\"]"))).send_keys(PHONE_NUMBER)
            

            WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test=\"next-button\"]"))).click()

            WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa=\"submit-profile-top-btn\"]"))).click()

            email_save(tempURL)
        except:
            pass


        CREATE_INDEX += 1

        sleep(3)

        # driver.get("https://www.upwork.com/nx/jobs/search/?q=web%20OR%20wordpress%20OR%20shopify%20OR%20ecommerce%20OR%20woocommerce%20OR%20wix%20OR%20webflow&sort=recency&t=0,1&amount=100-499,500-999,1000-4999,5000-&payment_verified=1")
        driver.get("https://www.upwork.com/nx/jobs/search/?sort=recency&t=1&payment_verified=1")

        # WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h2[class=\"my-0 p-sm-right job-tile-title\"]"))).click()
        sleep(5)
        driver.execute_script(f'document.querySelectorAll(\'h2[class="my-0 p-sm-right job-tile-title"]\')[0].click()')
        sleep(3)
        move_to_apply_url = driver.find_elements(By.TAG_NAME, 'h2')[1]

        job_desc = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"job-description break mb-0\"]")))
        job_desc_text = job_desc.find_element(By.CSS_SELECTOR, ":first-child").text
        print(job_desc_text)
        print("\n")

        url = move_to_apply_url.find_element(By.CSS_SELECTOR, ":first-child").get_attribute('href')
        print(url)
        driver.get(url)

        WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label=\"Apply Now\"]"))).click()

        close_button = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"up-btn mt-0 mb-0 up-btn-primary\"]")))
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

            # cover_letter_textarea = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea[aria-labelledby=\"cover_letter_label\"]")))
            # cover_letter_textarea.send_keys(response_chatgpt_array[0])

            textarea_elements = driver.find_elements(By.TAG_NAME, 'textarea')
            index_textarea = 0
            while(index_textarea < textarea_count):
                textarea_elements[index_textarea].send_keys(response_chatgpt_array[index_textarea])
                index_textarea += 1

            send_proposal_button = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"up-btn up-btn-primary m-0\"]")))
            send_proposal_button.click()

            WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"checkbox\"]"))).click()
            WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"up-btn up-btn-primary m-0 btn-primary\"]"))).click()
            WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"checkbox\"]"))).click()
            WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"up-btn up-btn-primary m-0 btn-primary\"]"))).click()


        sleep(1000)
    else:
        driver.execute_script('document.getElementsByClassName("mb-3 air3-btn air3-btn-secondary")[3].click()')
        driver.find_element(By.CSS_SELECTOR, "input[aria-labelledby=\"title-label\"]").send_keys(profile['professional'])
        sleep(2)
        driver.execute_script('document.querySelector(\'button[data-test="next-button"]\').click()')  # Add experience button
        #driver.execute_script("document.querySelectorAll('button.air3-btn.air3-btn-primary')[5].click()'")
        
        sleep(2)
        

        # driver.execute_script('document.getElementsByClassName("air3-btn air3-btn-lg air3-btn-secondary-inverted air3-btn-circle").click()')



        # driver.execute_script('document.querySelector("button.air3-btn.air3-btn-primary.mb-0").click()')
        # inp_prof = driver.find_element(By.CSS_SELECTOR, "input[data-test=\"title\"]")
        # # inp_prof.click()
        # inp_prof.send_keys(profile['professional'])
        # nexBtn = driver.find_element(By.CSS_SELECTOR, "button.air3-btn.air3-btn-primary")
        # clickByMouse(nexBtn)
        
        # driver.execute_script('document.querySelector("button.air3-btn.air3-btn-primary.mb-0").click()')
        sleep(9)
        # waitInfinite(lambda: driver.find_element(By.ID, "typeahead-input-75").send_keys(title))
        for i in profile['workXP']:
            addExperience(driver, *i)


        sleep(1)
        driver.execute_script('document.querySelector(\'button[data-test="next-button"]\').click()')    # Add education button

        sleep(1)
        driver.execute_script('document.querySelector(\'button[data-qa="education-add-btn"]\').click()')
        
        print("############QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ")

        expFlag = True
        sleep(1)
        for i in profile['education']:
            addEducation(driver, *i)

        # driver.execute_script('document.querySelector(\'button[data-test="next-button"]\').click()')  
        # driver.execute_script('document.querySelector("button.air3-btn.air3-btn-primary.mb-0").click()')

        expFlag = True
        sleep(1)
        waitInfinite(lambda: selectDateDropDown("dropdown-label-english", "span.air3-menu-item-text", 2))

        count = 0
        for i in profile['languages']:
            count = addLanguage(driver, *i, count)

        waitInfinite(lambda: driver.execute_script('document.querySelector("button.air3-btn.air3-btn-primary.mb-0").click()'))

        sleep(1)
        inp_skills = driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby="skills-input"]')
        
        for i in profile['skills']:
            addSkill(driver, inp_skills, i)

        waitInfinite(lambda: driver.execute_script('document.querySelector("button.air3-btn.air3-btn-primary.mb-0").click()'))

        sleep(1)
        waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, 'textarea[aria-labelledby="overview-label"]').send_keys(profile['overview']))
        sleep(0.5)
        clickByMouse(driver.find_element(By.CSS_SELECTOR, 'button.air3-btn.air3-btn-primary.mb-0'))
        # waitInfinite(lambda: driver.execute_script('document.querySelector("button.air3-btn.air3-btn-primary.mb-0").click()'))

        sleep(3)
        addService(driver, profile['services'])
        waitInfinite(lambda: driver.execute_script('document.querySelector("button.air3-btn.air3-btn-primary.mb-0").click()'))

        sleep(1)
        
        inp_hr = driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Hourly rate in $/hr"]')
        inp_hr.clear()
        inp_hr.send_keys(str(profile['hourRate']))
            
        waitInfinite(lambda: driver.execute_script('document.querySelector("button.air3-btn.air3-btn-primary.mb-0").click()'))
        
        sleep(1)
        configLast(
            driver,
            profile['location'],
            profile['street'],
            profile['city'],
            profile['zipcode'],
            profile['phone'],
            profile['avatar']
        )

        sleep(4)
        waitInfinite(lambda: driver.execute_script('document.querySelector("button.air3-btn.air3-btn-primary.mb-0").click()'))
        sleep(3)
        waitInfinite(lambda: driver.execute_script('document.querySelector("button.air3-btn.width-md.m-0.air3-btn-primary").click()'))

        driver.get("https://www.upwork.com/nx/find-work/best-matches/?landing=announcement-TONB-2806")

        try:
            open('email.txt', 'a', encoding='utf-8').write(tempURL + '\n')
        except FileNotFoundError:
            open('email.txt', 'w', encoding='utf-8').write(tempURL + '\n')

        print(tempURL)
        driver.close()
