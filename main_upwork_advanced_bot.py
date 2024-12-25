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
import get_resume_directory_filenames
import random

def main(create_account_count, campaign, searchPhase, sleep_time):
    SKILL_SET = [
        "Full-stack Development", "Zapier", "Data Scraping", "Web Scraping", "Data Extraction", "Bot Development", "Automation", "Selenium", "Beautiful Soup", "Scrapy", "Python", "Browser Automation",
        "Google Sheets Automation", "Web Scraping Framework", "Automation Anywhere", "Marketing Automation", "Web Scraping Plugin", "Web Scraping Software", "Screen Scraping", "Mozenda Scraper",
        "Scraper Site", "Robotic Process Automation", "Lead Generation", "Data Mining", "Python Script", "Data Cleaning", "API Integration", "Microsoft Excel", "Data Entry", "Google Search API",
        "List Building", "Scripts & Utilities", "Python-Requests", "Web Crawler"
    ]

    OVERVIEW_TEXT = ["Hello, I'm Assistant, a versatile and highly skilled professional with expertise in full-stack development, data scraping, web scraping, and bot development. With a strong background in Python and web scraping frameworks like Selenium, Beautiful Soup, and Scrapy, I'm capable of automating complex tasks and extracting valuable data from websites. Additionally, I specialize in browser automation and Google Sheets automation, utilizing my knowledge to streamline processes and enhance efficiency. Whether it's building AI bots or implementing marketing automation strategies, I bring a comprehensive skill set to deliver exceptional results.",
                     "Hey! Are you looking for someone to add value to your business through data scraping, data extraction, and web scraping solutions? So don't worry, you have found the expert scraper that you are looking for! I'm a expert, your go-to expert scraper for data extraction and web scraping solutions. If you're on the hunt for a data virtuoso to scrape and extract valuable insights for your business, you've just hit the jackpot.",
                     "I am AVAILABLE NOW and 24/7 \n Hi) I have been involved in commercial python development near 3 years. I add various services:\n# Scraping different web-pages\n# Automation scripts\n# development of any complexity on a python\n\nI love my job! I like to benefit people :)",
                     "I am a Data Engineer specializing in Web Scraping and Lead generation. And capable enough to extract millions of data from any business directory. I am done with 2500+ website scraping with 7+ years of experience.\nI can capable enough to handle any project belong to Web Scraping, Directory Scraping, Email Searching, Data Entry, Web Research, and Lead Generation, Product Scraping services.\nI have an expert at using Excel and Notepad++ to process and clean up extracted data. I can provide the scarped data in various formats such as CSV, Excel, JASON, Database file, etc.\nIt is important for me to build long-term relationships with clients, so I am primarily looking for long-term projects. I am flexible with my working hours and I am happy to work closely with any existing freelancers you work with.\nLooking forward to hearing from you!\nNote: I work hard to gain 100\'%\' satisfaction of my clientele through quality work. I am ready to give daily updates. I respect all the changes suggested by my clients. I respectfully include the changes in the projects to meet customer requirements.",
                     "I am an experienced Python developer with more than 5 years of hands-on expertise, especially in the areas of web scraping and Flask frameworks. My journey in the tech industry so far has been fueled by my passion for tackling complex projects and crafting efficient, innovative solutions.",
                     "Having more than 9 years of experience in web scraping, lead generation, data scraping, data processing, data extraction, scraping code writing and technical task automation and a total 12+ years of experience in information technologies.\nDuring the time of jobs and projects I had achieved lots of challenges and skills:\nGoogle captcha bypass, Image captcha bypass, Image OCR, IP rotation, Cookies handling, Session handling JavaScript bypass, PDF text extraction etc."]
    # MY_TITLE = "Senior Full-stack Developer | Data Scraping, Automation Expert"
    # MY_TITLE = campaign
    MY_TITLE = ["Senior Full-stack Developer | Data Scraping, Automation Expert",
                "Web Scraping, crawling, Python, data mining, and Lead Generation",
                "Data Scraping and Data Extraction through Web Scraping | Web scraper",
                "Expert of Data python-developer, scraping dev, back-end developer",
                "Web scraping Expert",
                "Web Scraping / Automation Expert / Data Extraction / Python Scraping",
                "Scraping Master - Python/Scrapy/Selenium",
                "Web Scraping Maestro: Turning Websites into Databases"]

    MY_HOURLY_RATE = 35

    # COUNTRY = 'Ukraine'
    COUNTRY = 'Canada'

    BID_MANUALS = ["Hi, I carefully read your requirements. I am sure that I am the most suitable one you are looking for. Can we have a meeting now and discuss further?", 
                   "Hello I am ready all neccessary skills for this project.\nI can help you so that you can save time.\nYour satisfaction is more important than money. \nSend me a message and I'll arrange a call at your convenience.\nI look forward to speaking soon.\nRegards.", 
                   "Hello.\nI can do it and I am ready to start your project right now.\nIf you hire me, I will start your project immediately and you would save time and money.\nPlease contact me and then let us discuss your project in more detail.", 
                   "Okay, I will do it. It's a simple job. I will make a bot for this project and it will takes about 3 hours", 
                   "Hi, I can do it. It takes about only 5 hours", 
                   "Hello, I can do it in 5 hours. Are you available to have a meeting now? I would like to discuss your project in more detail.\n Thank you",
                   "Hi, it's a simple job for me. I can do it in 3 hours. Please contact me"]

    # RESUME_PATH = "C:\\Auto Register\\resume\\1.pdf"
    # PHOTO_PATH = "C:\\Auto Register\\photo\\1.png"
    # RESUME_PATH = f"{getPath.get_project_path()}\\resume\\1.pdf"
    # PHOTO_PATH = f"{getPath.get_project_path()}\\photo\\{get_photo_directory_filenames.get_random_photo()}"

    BIRTH_OF_DATE = "1990-08-05"

    STREET_ADDRESS = ["130 rue Levy", "918 Burdett Avenue", "1573 Albert Street", "1712 No. 3 Road", "1465 9th Avenue", "2541 40th Street"]
    CITY_NAME = ["Montreal", "Terrace", "Kitchener", "Richmond", "Hanover", "Calgary"]
    PHONE_NUMBER = ["514-893-1337", "250-625-1695", "519-594-6242", "604-249-1676", "519-364-4817", "403-282-3010"]
    ZIP_CODE = ["H3C 5K4", "V8G 1S2", "N2L 3V2", "V6X 2B8", "N4N 2Z8", "T2M 0X4"]
    # STREET_ADDRESS = ["Dorofeeva Ul., bld. 4/А, appt. 128"]
    # CITY_NAME = ["Kherson"]
    # PHONE_NUMBER = ["+380(0552)27-00-25"]
    # ZIP_CODE = ["1700"]

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

    FILTERED_JOB_URL = f"https://www.upwork.com/nx/search/jobs?amount=100-499,500-999,45-4999,5000-&payment_verified=1&q={searchPhase}&sort=recency&t=0,1"
    # FILTERED_JOB_URL = f"https://www.upwork.com/nx/jobs/search/?q=I%20need%20scraping%20help%20as%20and%20when%20needed.%20Will%20never%20be%20super%20complicated%20work.%20%20I%20have%20a%20blog%20resource%20I%20want%20help%20with%20now%20to%20start.%2020%20pages-%20say%20an%20item%20has%20up%20to%206%20fields%20%28Guess%20about%20800%20rows%29.%20They%20are%20basically%20title,%20URL%20with%20categories.&sort=recency&payment_verified=1&per_page=10"
    # FILTERED_JOB_URL = f"https://www.upwork.com/nx/jobs/search/?sort=recency&payment_verified=1&per_page=10"


    index_question = 0

    file_path = 'bidTemplate.txt'
    file_extra_question_path = 'extraQuestion.txt'
    firefox_profile_directory = 'C:/Users/Administrator/AppData/Roaming/Mozilla/Firefox/Profiles/mled9ssy.default-release'
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

        if extra_questions_count != 0:
            firefox_driver = webdriver.Firefox(options=firefox_options)
            firefox_driver.maximize_window()
            firefox_driver.get("https://poe.com")

            input_chatgpt_text = WebDriverWait(firefox_driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea[class=\"GrowingTextArea_textArea__ZWQbP\"]")))
            input_chatgpt_text.send_keys(BID_REQUEST)

            WebDriverWait(firefox_driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"Button_buttonBase__Bv9Vx Button_primary__6UIn0 ChatMessageSendButton_sendButton__4ZyI4 ChatMessageInputContainer_sendButton__dBjTt\"]"))).click()

            WebDriverWait(firefox_driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"Button_buttonBase__Bv9Vx Button_tertiary__KEQm1 Button_iconOnly__poDNY\"]")))

            response_chatgpt = WebDriverWait(firefox_driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"Message_botMessageBubble__aYctV\"]:nth-child(1)")))
            response_chatgpt_result = response_chatgpt.find_element(By.CSS_SELECTOR, ":first-child")

            # bid_final = BeautifulSoup(response_chatgpt_result.get_attribute("innerHTML"), 'html.parser').get_text()

            bid_manuals_length = len(BID_MANUALS)
            bid_manuals_index = random.randint(0, bid_manuals_length - 1)

            bid_final = BID_MANUALS[bid_manuals_index]

            # bid_final = "Hi, I carefully read your requirements. I am sure that I am the most suitable one you are looking for. Can we have a meeting now and discuss further?"
            response_chatgpt_array.append(bid_final)
        
        if extra_questions_count == 0:
            # bid_final = "Hi, I carefully read your requirements. I am sure that I am the most suitable one you are looking for. Can we have a meeting now and discuss further?" 
            bid_manuals_length = len(BID_MANUALS)
            bid_manuals_index = random.randint(0, bid_manuals_length - 1)
            bid_final = BID_MANUALS[bid_manuals_index]
            response_chatgpt_array.append(bid_final)

        if extra_questions_count == 0:
            try:
                firefox_driver.quit()
            except: pass
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

    # proxy_usage = False
    # proxy_server = 'http://144.172.123.97:3128'
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument(f'--proxy-server={proxy_server}')

    SLEEP_TIME = sleep_time
    EMAIL_SAVE_TIME = sleep_time / 40

    while(CREATE_INDEX <= CREATE_PROFILE_COUNT):
        sleep(SLEEP_TIME)
        try:
            PHOTO_PATH = f"{getPath.get_project_path()}\\photo\\{get_photo_directory_filenames.get_random_photo()}"
            RESUME_PATH = f"{getPath.get_project_path()}\\resume\\{get_resume_directory_filenames.get_random_photo()}"

            emailGetter = webdriver.Chrome()

            #Get Temp URL

            emailGetter.get("https://www.minuteinbox.com/")
            tempURL = WebDriverWait(emailGetter, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[id=\"email\"]"))).text

            # driver = webdriver.Chrome() if not proxy_usage else webdriver.Chrome(options=chrome_options)
            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.get("https://www.upwork.com/nx/signup/?dest=home")
            
            # proxy_usage = not proxy_usage

            # sleep(5)
            # keyboard.press('tab')
            # keyboard.release('tab')
            # sleep(1.5)
            # keyboard.press('space')
            # keyboard.release('space')
            
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
                emailGetter.execute_script('x = document.querySelectorAll("td.from")[0];if(x.textContent == " Upwork Notifications ") x.click()')
                sleep(4)
                iframe = emailGetter.find_element(By.ID, "iframeMail")
                emailGetter.switch_to.frame(iframe)

            waitInfiniteEmailGetter(verifyEmail)
            verifiedURL = emailGetter.find_elements(By.TAG_NAME, 'a')[1].get_attribute('href')

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

                my_title_length = len(MY_TITLE)
                title_index = random.randint(0, my_title_length - 1)
                titleInput.send_keys(MY_TITLE[title_index])

                WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test=\"next-button\"]"))).click()
                WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test=\"next-button\"]"))).click()
                WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test=\"next-button\"]"))).click()

                selectDropDownPeriod("air3-dropdown-icon air3-icon md", "li.air3-menu-item", "Native or Bilingual")
                WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test=\"next-button\"]"))).click()
                sleep(5)

                WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[aria-labelledby=\"skills-input\"]")))


                def input_skills(skill, driv):
                    index = False
                    while(index == False):
                        skillsInput = (By.CSS_SELECTOR, "input[aria-labelledby=\"skills-input\"]")
                        skill_element = WebDriverWait(driv, 10).until(EC.presence_of_element_located(skillsInput))
                        try:
                            skill_element.click()
                            skill_element.clear()
                            skill_element.send_keys(skill)
                            skill_dropdown = WebDriverWait(driv, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul[class=\"air3-menu-list\"]")))
                            skill_dropdown.find_element(By.CSS_SELECTOR, ":first-child").click()
                            index = True
                        except:
                            # If the element becomes stale, re-locate it and try again
                            try:
                                skill_element = WebDriverWait(driv, 10).until(EC.presence_of_element_located(skillsInput))
                                skill_element.click()
                                skill_element.clear()
                                skill_element.send_keys(skill)
                                skill_dropdown = WebDriverWait(driv, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul[class=\"air3-menu-list\"]")))
                                skill_dropdown.find_element(By.CSS_SELECTOR, ":first-child").click()
                                index = True
                            except: pass

                random.shuffle(SKILL_SET)
                cut_skillset = SKILL_SET[:15]
                for skill in cut_skillset:
                    input_skills(skill, driver)

                sleep(2)

                WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test=\"next-button\"]"))).click()

                textArea_Overview = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea[aria-labelledby=\"overview-label\"]")))
                textArea_Overview.clear()

                overview_text_length = len(OVERVIEW_TEXT)
                overview_index = random.randint(0, overview_text_length - 1)
                textArea_Overview.send_keys(OVERVIEW_TEXT[overview_index])

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
                    upload_photo_button = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa=\"open-loader\"]")))
                    upload_photo_button.click()

                    parent_input = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"air3-image-crop-input-container is-empty\"]")))

                    input_photo = parent_input.find_element(By.TAG_NAME, "input")
                    input_photo.send_keys(PHOTO_PATH)
                    sleep(2)
                    save_button = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa=\"btn-save\"]")))
                    save_button.click()

                    sleep(10)
                    address_length = len(STREET_ADDRESS)
                    random_address_num = random.randint(0, address_length - 1)
                    # WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"air3-image-crop-area\"]")))
                    
                    birthday_input = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[aria-labelledby=\"date-of-birth-label\"]")))
                    # while(birthday_input.is_displayed() and birthday_input.is_enabled()):
                    #     sleep(1)
                    #     print("not")
                    birthday_input.send_keys(BIRTH_OF_DATE)
                    WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[aria-labelledby=\"street-label\"]"))).send_keys(STREET_ADDRESS[random_address_num])

                    city_name_input = (By.CSS_SELECTOR, "input[aria-labelledby=\"city-label\"]")
                    city_name_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(city_name_input))

                    index = False
                    while(index == False):
                        try:
                            city_name_element.click()
                            city_name_element.clear()
                            city_name_element.send_keys(CITY_NAME[random_address_num])
                            cityname_dropdown = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul[aria-labelledby=\"city-label\"]")))
                            cityname_dropdown.find_element(By.CSS_SELECTOR, ":first-child").click()
                            index = True
                            print("3")
                        except StaleElementReferenceException:
                            # If the element becomes stale, re-locate it and try again
                            city_name_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(city_name_input))
                            city_name_element.click()
                            city_name_element.clear()
                            city_name_element.send_keys(CITY_NAME[random_address_num])
                            cityname_dropdown = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul[aria-labelledby=\"city-label\"]")))
                            cityname_dropdown.find_element(By.CSS_SELECTOR, ":first-child").click()
                            index = True
                            print("4")

                    WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[aria-labelledby=\"postal-code-label\"]"))).send_keys(ZIP_CODE[random_address_num])
                    WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[inputmode=\"numeric\"]"))).send_keys(PHONE_NUMBER[random_address_num])
                    
                    sleep(2)
                    WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test=\"next-button\"]"))).click()

                    WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa=\"submit-profile-top-btn\"]"))).click()
                except:
                    pass

               
                def email_save_to_txt(email1):
                    with open(FILENAME, "a") as file:
                        file.write(email1 + "\n")
                        
                email_save_to_txt(tempURL)


                sleep(3)

                job_url = input("Please enter the job url: ")

                FILTERED_JOB_URL = job_url

                # driver.get("https://www.upwork.com/nx/jobs/search/?q=web%20OR%20wordpress%20OR%20shopify%20OR%20ecommerce%20OR%20woocommerce%20OR%20wix%20OR%20webflow&sort=recency&t=0,1&amount=100-499,500-999,45-4999,5000-&payment_verified=1")
                driver.get(FILTERED_JOB_URL)
                
                # sleep(1000)

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

                    job_desc = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-test=\"Description\"]")))
                    job_desc_text = job_desc.find_element(By.CSS_SELECTOR, ":first-child").text
                    print(job_desc_text)
                    print("\n")

                    driver.get(move_to_apply_url)

                WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label=\"Apply Now\"]"))).click()

                try:
                    close_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"air3-btn mt-0 mb-0 air3-btn-primary\"]")))
                    close_button.click()
                except:
                    close_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"up-btn mt-0 mb-0 up-btn-primary\"]")))
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
                        selectDropDownPeriod("air3-dropdown-icon air3-icon md", "li.air3-menu-item", "Never")
                        sleep(1)
                        driver.execute_script(f'document.querySelectorAll(\'span[data-test="checkbox-input"]\')[1].click()')
                    except:
                        pass
                if(job_type == "fixed"):
                    print("fix")
                    try:
                        selectDropDownPeriod("air3-dropdown-icon air3-icon md", "li.air3-menu-item", "Less than 1 month")
                        sleep(1)
                        driver.execute_script(f'document.querySelectorAll(\'span[data-test="checkbox-input"]\')[1].click()')
                    except:
                        pass

                textarea_count = len(driver.find_elements(By.TAG_NAME, 'textarea'))
                # print(textarea_count)

                array_extra_questions = []

                textarea_label = driver.find_elements(By.CSS_SELECTOR, 'label.label')
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
                        send_proposal_button = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"air3-btn air3-btn-primary m-0\"]")))
                        send_proposal_button.click()
                except:
                    pass
                
                if bid_amount != 50:
                    send_proposal_button = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"air3-btn air3-btn-primary m-0\"]")))
                    send_proposal_button.click()
                    numbers = re.findall(r'\d+', send_proposal_button.text)
                    numbers = [int(num) for num in numbers]
                    print(numbers)
                    bid_amount = numbers[0]
                try:
                    # driver.execute_script(f'document.querySelector(\'span[data-test="checkbox-input"]\').click()')
                    try:
                        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[class=\"air3-checkbox-label\"]"))).click()
                    except:
                        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[class=\"ml-4x mt-4x air3-checkbox-label\"]"))).click()
                    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"air3-btn air3-btn-primary m-0 btn-primary\"]"))).click()
                    sleep(2)

                    try:
                        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[class=\"air3-checkbox-label\"]"))).click()
                    except:
                        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[class=\"ml-4x mt-4x air3-checkbox-label\"]"))).click()
                    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"air3-btn air3-btn-primary m-0 btn-primary\"]"))).click()
                except:
                    pass

                sleep(3)
                sleep(EMAIL_SAVE_TIME)
                email_save(tempURL)
                quickstart.main()
                quickstart.getProfileData()
                columnCount1 = quickstart.getColumnCount()
                # start_index_to_insert_bid_status = columnCount + 1
                quickstart.insertBidStatusData(f'upwork profile!C{columnCount1}:C', bid_amount)

                driver.quit()
                sleep(5)
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
            # driver.quit()
    return tempURL, first_name, last_name, PHOTO_PATH, MY_HOURLY_RATE, bid_amount, job_desc_text, response_chatgpt_array