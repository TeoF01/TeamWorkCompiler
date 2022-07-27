import selenium
from selenium.webdriver.common.keys import Keys


def clear_date_input(date_label: selenium.webdriver.remote.webelement.WebElement) -> [None]:
    date_label.send_keys(Keys.COMMAND + 'a')
    date_label.send_keys(Keys.BACKSPACE)
