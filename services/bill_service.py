from services.generic_service import delay
from selenium.webdriver.common.by import By


def not_billable_option(BROWSER) -> [None]:
    """This function un-flag the billable option"""
    delay(1)
    BROWSER.find_element(By.ID, 'm-add-edit-time-entry-billable').click()
    delay(0.5)
