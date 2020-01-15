class MyStriungException(Exception):
    def __init__(self, message, error):
        self._message = message
        self._error = error
        super().__init__()

    @property
    def message(self):
        return self._message

    @property
    def error(self):
        return self._error

    def __str__(self):
        return self._message

def input_str(string):
    if len(string) < 1:
        raise MyStriungException("len must be more than 0", 'empyt string')

try:
    input_str('')
except MyStriungException as e:
    print(e.error)
    print(e.message)
    print(e)
