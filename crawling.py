from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

browser = webdriver.Firefox()


file = open('companylist.csv','r')
with file as f:
    next(f)
    for line in f:
        ticker = line.split(",")[0].replace("\"","")
        browser.get('http://finance.yahoo.com/quote/'+ticker+'?p='+ticker)
        try:
            elem = browser.find_element_by_class_name('rating-text')
            print(ticker+","+elem.text)
        except NoSuchElementException:
            print("Skip")

file.close()
browser.quit()
