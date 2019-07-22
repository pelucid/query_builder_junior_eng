import re
from query_builder import exceptions
from query_builder.app.handlers.base_filter import BaseFilter


class Boolean(BaseFilter):

    def __init__(self, *args, **kwargs):
        super(Boolean, self).__init__(*args, **kwargs)
        self.bool_val = None

    def _parse(self):
        if not self.url_value:
            return
        arg_check_int = re.search("^[0-1]$", self.url_value)
        arg_check_bool = re.search("^true|false", self.url_value.lower())
        if arg_check_int:
            self.bool_val = bool(int(self.url_value))
        elif arg_check_bool:
            self.bool_val = {"true": True, "false": False}[self.url_value.lower()]
        else:
            raise exceptions.ParameterValueError(key=self.url_key, value=self.url_value)

    def _validate(self):
        pass

    def serialise(self):
        pass


