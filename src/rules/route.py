import time

from src.driver_init import MyDriver
from src.rules.common import open_url, close_test

driver = MyDriver('Firefox')

open_url(driver)


def click_routing():
    driver.get_driver().find_element_by_css_selector(
        "#sidebar > div:nth-child(1) > form:nth-child(1) > a:nth-child(1)").click()


def set_route_origin(origin):
    driver.get_driver().find_element_by_css_selector(
        '#sidebar > div:nth-child(1) > form:nth-child(2) > div:nth-child(2) > span:nth-child(2) > input:nth-child(1)') \
        .send_keys(origin)


def set_route_destination(destination):
    driver.get_driver().find_element_by_css_selector(
        '#sidebar > div:nth-child(1) > form:nth-child(2) > div:nth-child(3) > span:nth-child(2) > input:nth-child(1)') \
        .send_keys(destination)


def calculate_route():
    driver.get_driver().find_element_by_xpath("/html/body/div/div[1]/div[1]/form[2]/div[4]/select").click()


def get_route_info():
    info = driver.get_driver().find_element_by_css_selector("#routing_summary").text.splitlines()
    print(info)


def change_route_profile(profile):
    profiles = dict(bike_graph=1,
                    bike=2,
                    car_graph=3,
                    car=4,
                    foot=5,
                    foot_graph=6)

    driver.get_driver().find_element_by_xpath(
        "/html/body/div/div[1]/div[1]/form[2]/div[4]/select/option[" + str(profiles.get(profile)) + "]").click()


click_routing()
set_route_origin('Cluj')
set_route_destination('Bistrita')
change_route_profile('bike')
calculate_route()
time.sleep(2.0)
get_route_info()
close_test(driver)
