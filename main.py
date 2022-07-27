import logging

from selenium.webdriver.common.by import By

from browser_config.browser_data import URL, BROWSER
from data_to_log import dataa
from services import login_service
from services.bill_service import not_billable_option
from services.date_service import clear_date_input
from services.description_service import post_description
from services.generic_service import close_session, search_html_element, click_element, go_to_task
from services.log_time_service import click_log_time

log = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO,
                    style='{',
                    format='{asctime} -- {levelname} = {message}',
                    datefmt='%I:%M:%S %p'
                    )


def main_process():
    try:
        log.info(msg=f'Start Time')
        login_service.login(BROWSER=BROWSER, url=URL)
        go_to_task(browser=BROWSER, url=URL)

        for data in dataa:
            click_log_time(BROWSER=BROWSER)
            not_billable_option(BROWSER=BROWSER)

            date_input = search_html_element(browser=BROWSER, criterion=By.CLASS_NAME, param='w-date-input__input')
            if date_input:
                click_element(date_input)
                clear_date_input(date_input)
                date_input.send_keys(data[0])
            else:
                log.error(msg=f'Element date_input not found..')
                raise Exception

            description_label = search_html_element(browser=BROWSER, criterion=By.LINK_TEXT, param='Description')
            if description_label:
                click_element(description_label)
            else:
                log.error(msg=f'Element description_label not found..')
                raise Exception

            start_time = search_html_element(browser=BROWSER, criterion=By.CLASS_NAME, param='time-input')
            if start_time:
                click_element(start_time)
                start_time.send_keys(data[1])
            else:
                log.error(msg=f'Element start_time not found..')
                raise Exception

            end_time = BROWSER.find_elements(By.CLASS_NAME, 'time-input')[1]
            end_time.click()
            end_time.send_keys(data[2])

            post_description(BROWSER=BROWSER, desc=str(data[3]))

            # insert_button = search_html_element(browser=BROWSER, criterion=By.CLASS_NAME, param='action')
            # if insert_button:
            #     click_element(insert_button)
            # else:
            #     log.error(msg=f'Element insert_button not found..')
            #     raise Exception

        close_session(BROWSER=BROWSER)
        log.info(msg=f'End Time')
    except Exception as err:
        close_session(BROWSER)
        log.error(msg=str(err))
        raise err


main_process()
