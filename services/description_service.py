from selenium.webdriver.common.by import By


def post_description(BROWSER, desc: str):
    BROWSER.find_element(By.LINK_TEXT, 'Description').click()
    label = BROWSER.find_element(By.ID, 'addOrEditTimeEntryDescriptionInput')
    label.click()
    label.send_keys(desc)
