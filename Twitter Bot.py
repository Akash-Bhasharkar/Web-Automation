from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
import time
import os

U_SPEED = 50  #Upload Speed of your wifi
D_SPEED = 40  #Download speed of your wifi

EMAIL = "" #Login Id for Twitter
PASSWORD = ""          #Password

chrome_driver_path = "C:/Akki/chromedriver"

driver = webdriver.Chrome(executable_path = chrome_driver_path)

driver.get("https://www.speedtest.net/")

go = driver.find_element_by_xpath("//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a")
go.click()

time.sleep(40)

download_speed = driver.find_element_by_xpath("//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")
d_speed = float(download_speed.text)

upload_speed = driver.find_element_by_xpath("//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span")
u_speed = float(upload_speed.text)

if U_SPEED > u_speed or D_SPEED > d_speed :
    driver.get("https://twitter.com/i/flow/login")
    time.sleep(5)

    mail = driver.find_element_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input")
    mail.send_keys(EMAIL)
    mail.send_keys(Keys.ENTER)


    time.sleep(5)

    password = driver.find_element_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input")
    password.send_keys(PASSWORD)
    password.send_keys(Keys.ENTER)

    time.sleep(10)

    compose = driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div")
    compose.send_keys("Low speed") #Tweet

    tweet = driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]")
    tweet.click()
