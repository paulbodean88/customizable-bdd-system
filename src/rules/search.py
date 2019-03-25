import time

from src.driver_init import MyDriver
from src.rules.common import open_url, close_test

driver = MyDriver('Firefox')
open_url(driver)


def set_query(query):
    driver.get_driver().find_element_by_css_selector(
        "#sidebar > div:nth-child(1) > form:nth-child(1) > div:nth-child(3) > input:nth-child(1)").send_keys(query)


set_query('Cluj')


def click_search():
    driver.get_driver().find_element_by_css_selector(
        "#sidebar > div:nth-child(1) > form:nth-child(1) > input:nth-child(2)").click()


click_search()

time.sleep(2.0)


def validate_content(expected):
    list_content = driver.get_driver().find_element_by_xpath("/html/body/div/div[1]/div[5]/div[1]/ul").text.splitlines()
    [print(True) for l in list_content if expected in l]


validate_content('Cluj')
close_test(driver)
