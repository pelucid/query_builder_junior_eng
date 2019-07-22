import re
from query_builder import exceptions
from query_builder.app.handlers.base_filter import BaseFilter


class Boolean(BaseFilter):

    def __init__(self, key, value, include_if_false=True, **kwargs):
        super(Boolean, self).__init__(key, value)
        self.bool_val = None
        self.include_if_false = include_if_false

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
        if not (self.include_if_false or self.bool_val):
            return {}
        else:
            return {self.url_key: self.bool_val}
