
class ExecutionData(dict):

    def __init__(self, input_data: dict,
                 expected_data: dict, additional_data: dict, **kwargs):

        super().__init__(**kwargs)
        self.input = input_data
        self.expected = expected_data
        self.additional_data = additional_data
        self['INPUT'] = input_data
        self['EXPECTED'] = expected_data
        self['ADDITIONAL_DATA'] = additional_data
