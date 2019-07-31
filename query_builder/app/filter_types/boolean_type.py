import re

from base_filter import BaseFilter
from query_builder import exceptions


class BooleanType(BaseFilter):
    def __init__(self, *args, **kwargs):
        super(BooleanType, self).__init__(*args, **kwargs)
        self.booleanreturn = None
        self.includeiffalse = kwargs['include_if_false']


    def _parse(self):

        arg_check_int = re.search("^[0-1]$", self.url_value)
        arg_check_bool = re.search("^true|false", self.url_value.lower())
        if arg_check_int:
            self.booleanreturn = bool(int(self.url_value))
        elif arg_check_bool:
            self.booleanreturn = {"true": True, "false": False}[self.url_value.lower()]
        else:
            raise exceptions.ParameterValueError(key=self.url_key, value=self.url_value)


    def _validate(self):
        if not isinstance(self.booleanreturn, bool):
            raise exceptions.ParameterValueError(key=self.url_key, value=self.url_value)

    def serialise(self):
        if self.booleanreturn or self.includeiffalse:
            return {self.url_key: self.booleanreturn}
        return {}