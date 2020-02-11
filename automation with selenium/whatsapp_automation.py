from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_path = r"C:\Users\91907\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get("https://web.whatsapp.com/")
name=input("Enter the contact name:  ")
test = driver.find_element_by_xpath('//span[contains(@title,"{}")]'.format(name))
test.click()


msg=input("Enter message to send:  ")

textbox = driver.find_element_by_class_name('_13mgZ')
for i in range (4):

    textbox.send_keys(msg)
    
    time.sleep(5)
    textbox.send_keys()
    time.sleep(5)
    btn = driver.find_element_by_class_name('_3M-N-')
    btn.click()
    time.sleep(5)