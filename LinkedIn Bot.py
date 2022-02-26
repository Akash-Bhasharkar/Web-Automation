from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:/Akki/chromedriver"

driver = webdriver.Chrome(executable_path = chrome_driver_path)
driver.get("https://www.linkedin.com/")

EMAIL = ""    #Login Id for LinkedIn
PASSWORD = "" #Password

time.sleep(3)
verify = driver.find_element_by_class_name("nav__button-secondary")
verify.click()
time.sleep(3)
email = driver.find_element_by_name("session_key")
password = driver.find_element_by_name("session_password")

email.send_keys(EMAIL)
password.send_keys(PASSWORD)
time.sleep(3)
sign_in = driver.find_element_by_class_name("btn__primary--large")
sign_in.click()

time.sleep(3)

jobs = driver.find_element_by_xpath("//*[@id='ember20']")
jobs.click()

time.sleep(3)

search = driver.find_element_by_xpath("//*[@id='global-nav-search']/div/div[2]/button[1]")
search.click()

time.sleep(3)

job_list = driver.find_elements_by_css_selector(".job-card-container--clickable")

for job in job_list : 
    time.sleep(3)  
    job.click()
    try : 
        time.sleep(3)
        apply = driver.find_element_by_class_name("jobs-apply-button")
        apply.click()
        time.sleep(3)
        ph_no = driver.find_element_by_class_name("fb-single-line-text__input")
        if ph_no.text == "" :
              ph_no.send_keys("1234567890")
        time.sleep(3)
        submit = driver.find_element_by_css_selector("footer button")
        submit.click()
        time.sleep(5)
        close = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close.click()
    except NoSuchElementException or StaleElementReferenceException :
        time.sleep(3)
        try :   
           close = driver.find_element_by_class_name("artdeco-modal__dismiss")
           close.click()
           discard = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")
           discard[1].click()
        except NoSuchElementException : 
            pass
        


