from selenium import webdriver
from selenium.webdriver.common.by import By
from settings import settings

driver = webdriver.Chrome('C:/Program Files (x86)/chromedriver/chromedriver.exe')

def login_form():
    driver.get(settings['url'])
    driver.find_element_by_xpath('//input[@id=\"email\"]').send_keys(settings['login']) 
    driver.find_element_by_xpath('//input[@id=\"pass\"]').send_keys(settings['password'])   
    #driver.find_element(By.XPATH, '//input[@name="email"]').send_keys(settings['login'])
    #driver.find_element(By.XPATH, '//input[@name="pass"]').send_keys(settings['password'])
    driver.find_element_by_xpath('//button[@name=\"login\"]').click()

def send_message(message):
    driver.find_element_by_xpath('//br[@data-text=\"true\"]').send_keys(message)
    driver.find_element_by_xpath('//a[aria-label=\"Wyślij\"]').click()

login_form()
