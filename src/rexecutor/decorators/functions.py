import json

from src.rexecutor.data_models.rule_data import RuleResult


def ui_rule(func):
    def wrapper(**kwargs):
        identifier_data = json.load(open(kwargs['rule_config']['config']))
        kwargs['ids'] = identifier_data

        driver = kwargs['rule_config']['driver']

        try:
            element_id_path = kwargs['ids'][kwargs['rule_value']]
            element = None

            if element_id_path.startswith("#"):
                element = driver.find_element_by_css_selector(element_id_path)
            elif element_id_path.startswith("/"):
                element = driver.find_element_by_xpath(element_id_path)

            if 'input_key' in kwargs['rule_config']:
                kwargs['INPUT'] = kwargs['INPUT']['data'][kwargs['rule_config']['input_key']]
            else:
                kwargs['INPUT'] = kwargs['INPUT']['data']

            if 'expected_key' in kwargs['rule_config']:
                kwargs['EXPECTED'] = kwargs['EXPECTED']['data'][kwargs['rule_config']['expected_key']]
            else:
                kwargs['EXPECTED'] = kwargs['EXPECTED']['data']

            result = func(element, **kwargs)
            result['rule'] = kwargs['rule_name']

            return result

        except Exception as e:
            return RuleResult(RuleResult.FAILED,
                              rule=kwargs['rule_name'],
                              input=kwargs['rule_value'],
                              exception=str(e))

    return wrapper
