import time

from selenium import webdriver

from src.rexecutor.data_models.rule_data import RuleResult
from src.rexecutor.decorators.functions import ui_rule
from src.rexecutor.rules.rule_model import RuleModel


class OSMDriver(object):
    __driver = None

    @staticmethod
    def get_driver():
        if OSMDriver.__driver is None:
            OSMDriver.__driver = webdriver.Firefox(executable_path='./resources/geckodriver')
            OSMDriver.__driver.get("https://www.openstreetmap.org")

            time.sleep(2)
        return OSMDriver.__driver

    @staticmethod
    def reset():
        OSMDriver.__driver = None


@ui_rule
def check_element_exists(element, **kwargs):
    if element is not None:
        return RuleResult(RuleResult.PASSED)
    else:
        return RuleResult(RuleResult.FAILED)


@ui_rule
def type_text(element, **kwargs):
    element.send_keys(kwargs['INPUT'])

    return RuleResult(RuleResult.PASSED)


@ui_rule
def click_on(element, **kwargs):
    element.click()

    return RuleResult(RuleResult.PASSED)


@ui_rule
def validate_search(element, **kwargs):
    try:
        result_items_ul = element.find_element_by_tag_name("ul")
        result_items = result_items_ul.find_elements_by_tag_name("li")

        for item in result_items:
            if kwargs['EXPECTED'].upper() not in str(item.text).upper():
                return RuleResult(RuleResult.FAILED, expected=kwargs['EXPECTED'], input=str(item.text))

        return RuleResult(RuleResult.PASSED)

    except Exception as e:
        return RuleResult(RuleResult.FAILED, exception=str(e))


@ui_rule
def check_route_summary(element, **kwargs):
    print(element.text)
    return RuleResult(RuleResult.PASSED)


def on_done():
    driver = OSMDriver.get_driver()
    driver.quit()
    OSMDriver.reset()


class Rules(object):

    @staticmethod
    def get_rules_dict():
        rule_dict = {
            'check element {} exists': RuleModel(check_element_exists, driver=OSMDriver.get_driver(), config='resources/identifiers.json'),
            'search in {}': RuleModel(type_text, input_key='address', driver=OSMDriver.get_driver(), config='resources/identifiers.json'),
            'click on {}': RuleModel(click_on, driver=OSMDriver.get_driver(), config='resources/identifiers.json'),
            'validate result in container {}': RuleModel(validate_search, expected_key='address', driver=OSMDriver.get_driver(), config='resources/identifiers.json'),
            'set route origin in {}': RuleModel(type_text, input_key='origin', driver=OSMDriver.get_driver(), config='resources/identifiers.json'),
            'set route destination in {}': RuleModel(type_text, input_key='destination', driver=OSMDriver.get_driver(), config='resources/identifiers.json'),
            'set route profile to {}': RuleModel(click_on, driver=OSMDriver.get_driver(), config='resources/identifiers.json'),
            'check route summary {}': RuleModel(check_route_summary, driver=OSMDriver.get_driver(), config='resources/identifiers.json'),
        }

        return rule_dict
