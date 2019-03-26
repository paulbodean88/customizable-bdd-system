import re
import time

from src.rexecutor.data_models.execution_data import ExecutionData
from src.rexecutor.data_models.rule_data import RuleResult
from src.rexecutor.utilities.flow_iterator import Flow


class RuleExecutor(object):

    def __init__(self, rules_file: str, rules: dict, global_keys: list = None):
        self._flow = Flow(rules_file)
        self._rules = rules
        self.global_keys = global_keys
        self.__on_done_callback = None

    def set_on_done(self, on_done):
        self.__on_done_callback = on_done

    def execute(self, rule: str, execution_data: ExecutionData) -> RuleResult:
        rule_name_data = re.search(r'{(.*)}', rule)
        generic_rule = re.sub(r'{.*}', "{}", rule)
        method_data = {'rule_name': rule,
                       'rule_config': {**self._rules[generic_rule].format()['config']},
                       **execution_data}

        if len(rule_name_data.groups()) > 0:
            method_data['rule_value'] = rule_name_data.group(1)

        return self._rules[generic_rule].format()['method'](**method_data)

    def execute_flow(self, execution_data: ExecutionData):
        one_run_result = list()

        while self._flow.has_rules():
            rule = self._flow.next_rule()
            try:
                print(">> executing", rule)
                result = self.execute(rule, execution_data)
                time.sleep(1)
                one_run_result.append(result)

            except Exception as e:
                result = {'status': 'Failed', 'rule': rule, 'exception': str(e)}
                one_run_result.append(result)
                if self.__on_done_callback is not None:
                    self.__on_done_callback()

            try:
                self._flow.move_to(result['status'])
            except KeyError:
                raise KeyError('Rule result: '+str(result['status'])+' not specified for rule: '+rule)

        if self.__on_done_callback is not None:
            self.__on_done_callback()

        flow_status = self._flow.get_current_level()['@status']
        self._flow.reset()
        global_data = {}
        return {'status': flow_status, **global_data, 'data': one_run_result}
