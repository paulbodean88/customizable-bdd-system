
class RuleModel(object):

    def __init__(self, method_callback, **kwargs):
        self._method_callback = method_callback
        self._config = {**kwargs}

    def format(self) -> dict:
        return {'method': self._method_callback,
                'config': self._config}
