from selenium.webdriver.common.by import By

from .generic_service import delay


def click_log_time(BROWSER):
    delay(2)
    log_time_button = BROWSER.find_element(By.CLASS_NAME, 'main-header__base')\
        .find_element(By.CLASS_NAME, 'main-header__right')\
        .find_elements(By.CLASS_NAME, 'btn-secondary')[1]
    log_time_button.click()


