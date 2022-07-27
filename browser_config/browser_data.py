import os
from selenium import webdriver


URL = os.getenv('url')

BROWSER = webdriver.Chrome('browser_config/driver/chromedriver')
