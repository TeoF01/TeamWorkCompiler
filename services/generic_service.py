import time
import selenium

def delay(sec: float):
    time.sleep(sec)


def close_session(BROWSER):
    BROWSER.close()


def search_html_element(browser, criterion, param):
    element = browser.find_element(criterion, param)
    return element

def click_element(element: selenium.webdriver.remote.webelement.WebElement):
    element.click()


def go_to_task(browser, url):
    delay(2.0)
    browser.get(f'{url}#/tasks/23197631')
