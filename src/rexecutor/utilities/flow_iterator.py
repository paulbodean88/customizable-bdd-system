import xmltodict


class Flow(object):
    def __init__(self, rules_file):
        self.__rules_file = rules_file
        file_descriptor = open(rules_file, 'r')
        self._flow = xmltodict.parse(file_descriptor.read())
        file_descriptor.close()

    def next_rule(self):
        return self._flow['Rule']['@name']

    def move_to(self, status):
        self._flow = self._flow['Rule'][status]

    def has_rules(self):
        return 'Rule' in self._flow

    def reset(self):
        file_descriptor = open(self.__rules_file, 'r')
        self._flow = xmltodict.parse(file_descriptor.read())
        file_descriptor.close()

    def get_current_level(self):
        return self._flow
