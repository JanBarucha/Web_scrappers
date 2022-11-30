import emailSender
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import re


service = Service('Users\Janba\Downloads\chromedriver_win32')
browser = webdriver.Chrome(service=service)

url = 'https://www.cw-mobile.de/ember-travel-mug2-355-ml-thermoskanne-mit-wunschtemperatur-schwarz.html'

browser.get('https://www.cw-mobile.de/ember-travel-mug2-355-ml-thermoskanne-mit-wunschtemperatur-schwarz.html')


"""
Find mug price 
"""
value_path = '//*[@id="product-price-30270"]/span'

price = browser.find_element(by=By.XPATH, value=value_path)

actual_price = int(re.match('\d\d\d',price.text).group())

if actual_price < 200:
    emailSender.send_notification_mail(url)



