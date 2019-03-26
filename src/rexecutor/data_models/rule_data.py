
class RuleResult(dict):

    PASSED = "Passed"
    FAILED = "Failed"
    WARNING = "Warning"

    def __init__(self, status, **kwargs):
        super().__init__(**kwargs)
        self['status'] = status
