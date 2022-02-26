from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime  as dt
from datetime import timedelta
import time

chrome_driver_path = "C:/Akki/chromedriver"

driver = webdriver.Chrome(executable_path = chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")


time_ = dt.datetime.now()
end_time = time_ + timedelta(minutes = 1)
timeout = time.time() + 5

cookie = driver.find_element_by_id("cookie")




while  end_time >=dt.datetime.now() :
      cookie.click()
      
      cookies_text = driver.find_element_by_id("money")
      current_cookies = str(cookies_text.text)
      if "," in current_cookies : 
            current_cookies = int(cookies_text.text.replace(",", ""))
      else :
            current_cookies = int(cookies_text.text)
      if current_cookies >= 15 :
            if time.time() > timeout :
                  list_of_offers_text = driver.find_elements_by_css_selector("#store  b")
                  del list_of_offers_text[-1]
                  offers = []
                  buys = []
                  for items in list_of_offers_text :
                        money = str(items.text)
                        name = items.text.split("-")[0].strip()
                        if "," in money :
                            money = int(items.text.split("-")[1].strip().replace(",", ""))
                        else : 
                            money = int(items.text.split("-")[1].strip())
                        offers.append(money)
                        buys.append(name)
                  available_offers = []
                  for item in offers:
                      if item < current_cookies :
                         available_offers.append(item)
                  max_offer = max(available_offers)
                  index = available_offers.index(max_offer)
                  if len(available_offers) != 0 :
                        to_click = driver.find_element_by_id(f'buy{buys[index]}')
                        to_click.click()
                  timeout = time.time() + 5
                  

      

per_sec_text = driver.find_element_by_css_selector("#cps")
per_sec = float(per_sec_text.text.split(" :")[1])





        



