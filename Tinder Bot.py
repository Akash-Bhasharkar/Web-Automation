from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

F_ID = "" #Login Id for facebook
F_PASS = ""           #Password


chrome_driver_path = "C:/Akki/chromedriver"

driver = webdriver.Chrome(executable_path = chrome_driver_path)
driver.get("https://tinder.com/")

try : 

    time.sleep(3)
    Accept = driver.find_element_by_xpath("//*[@id='s1502865376']/div/div[2]/div/div/div[1]/button")
    Accept.click()

except NoSuchElementException :
       pass
      
time.sleep(2)

log_in = driver.find_element_by_css_selector("header .button")
log_in.click()

try : 

    time.sleep(3)
    facebook = driver.find_element_by_xpath("//*[@id='s-225515700']/div/div/div[1]/div/div[3]/span/div[2]/button")
    facebook.click()

except NoSuchElementException :
    
    time.sleep(3)
    more_options = driver.find_element_by_xpath("//*[@id='s192874960']/div/div/div[1]/div/div[3]/span/button")
    more_options.click()

    time.sleep(3)
    facebook = driver.find_element_by_xpath("//*[@id='s192874960']/div/div/div[1]/div/div[3]/span/div[2]/button")
    facebook.click()
    time.sleep(3)

windows = driver.window_handles

base_window = windows[0]
facebook_window = windows[1]

driver.switch_to.window(facebook_window)
email = driver.find_element_by_xpath("//*[@id='email']")
email.send_keys(F_ID)

password = driver.find_element_by_xpath("//*[@id='pass']")
password.send_keys(F_PASS)

f_log_in  = driver.find_element_by_name("login")
f_log_in.click()

windows = driver.window_handles
time.sleep(3)
base_window = windows[0]
driver.switch_to.window(base_window)

time.sleep(3)
allow = driver.find_element_by_xpath("//*[@id='s192874960']/div/div/div/div/div[3]/button[1]")
allow.click()

time.sleep(3)

no = driver.find_element_by_xpath("//*[@id='s192874960']/div/div/div/div/div[3]/button[2]")
no.click()
time.sleep(10)
reject = driver.find_element_by_xpath("//*[@id='s-2061886532']/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button")
on = True
while on : 
      try : 
          time.sleep(2)
          reject.click()

      except NoSuchElementException :
             on = False
      except ElementClickInterceptedException :
             time.sleep(2)
             no_intrest = driver.find_element_by_xpath("//*[@id='s192874960']/div/div/div[2]/button[2]")
             no_intrest.click()
             time.sleep(2)

          
          

