import json

from src.rexecutor.data_models.execution_data import ExecutionData
from src.rexecutor.executor import RuleExecutor
from src.rules import Rules, on_done

flow = 'routing_flow'
xml_flow_file = "resources/flows/{}.xml".format(flow)

testdata = json.load(open('resources/testdata.json'))

for data in testdata[flow]:
    execution_data = ExecutionData({'data': data['input']}, {'data': data['expected']}, {})

    executor = RuleExecutor(xml_flow_file, Rules.get_rules_dict())
    executor.set_on_done(on_done)

    print("flow execution report>", executor.execute_flow(execution_data))
    print()

if __name__ == '__main__':
    pass
