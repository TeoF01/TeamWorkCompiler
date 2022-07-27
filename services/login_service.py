import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from .generic_service import delay

TW_PASSWORD = os.getenv('psw')
TW_MAIL = os.getenv('email')


def login(BROWSER, url):
    BROWSER.get(url)
    delay(1.0)
    mail = BROWSER.find_element(By.ID, 'loginemail')
    mail.click()
    mail.send_keys(TW_MAIL)
    psw = BROWSER.find_element(By.ID, 'loginpassword')
    psw.click()
    psw.send_keys(TW_PASSWORD)
    login_button = BROWSER.find_element(By.CLASS_NAME, 'w-button__label')
    login_button.click()
