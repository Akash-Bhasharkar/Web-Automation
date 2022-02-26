
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
import time

ID = "" #Login Id for Instagram
PASSWORD = ""       #Password

chrome_driver_path = "C:/Akki/chromedriver"

class Bot :

    def __init__(self) :
    
        self.driver = webdriver.Chrome(executable_path = chrome_driver_path)
        self.driver.get("https://www.instagram.com/")

    
    def login(self) :

        email = self.driver.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
        email.send_keys(ID)

        password = self.driver.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")
        password.send_keys(PASSWORD)

        log_in = self.driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button")
        log_in.click()


    def search(self) :
        try:
            ignore = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")
            ignore.click()
        except NoSuchElementException:
            pass
        finally:
            search = self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
            search.send_keys("chefsteps")
            
            time.sleep(2)

            account = self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a")
            account.click()

            time.sleep(2)

    def follow(self) :
        
        followers = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a")
        followers.click()
        
        time.sleep(5)

        followers_list = self.driver.find_elements_by_css_selector("div li button")
        print(followers_list)

        for buttons in followers_list :
            buttons.click()
            time.sleep(2)

        time.sleep(2)

        close = self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div[1]/div/div[2]/button")
        close.click()

    def scroll(self) :

        for i in range(10) :
            time.sleep(2)
            target_element = self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div[2]//a")
            target_element.send_keys(Keys.END)