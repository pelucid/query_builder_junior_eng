import re

from query_builder import exceptions


class BaseFilter(object):
    def __init__(self, url_key, url_value, *args, **kwargs):
        self.url_key = url_key
        self.url_value = url_value

    def parse_and_validate(self):
        self._parse()
        self._validate()

    def _parse(self):
        raise NotImplementedError

    def _validate(self):
        raise NotImplementedError

    def serialise(self):
        raise NotImplementedError


class NumericRange(BaseFilter):
    def __init__(self, *args, **kwargs):
        super(NumericRange, self).__init__(*args, **kwargs)
        self.lower = None
        self.upper = None

    def _parse(self):
        if not self.url_value:
            return

        exp = re.compile(r"^(\-?[0-9]+)?\-(\-?[0-9]+)?$")
        m = re.search(exp, self.url_value)
        if not m:
            raise exceptions.ParameterValueError(key=self.url_key, value=self.url_value,
                                                 message="Does not match expected format")

        # Parse lower bound
        if m.group(1):
            self.lower = self._parse_match(m.group(1))

        # Parse upper bound
        if m.group(2):
            self.upper = self._parse_match(m.group(2))

    def _parse_match(self, matched_group):
        try:
            return int(matched_group)
        except ValueError:
            raise exceptions.ParameterValueError(key=self.url_key, value=self.url_value,
                                                 message="Cannot convert value to int")

    def _validate(self):
        """Validate Lower is not greater than Upper"""
        if self.lower is not None and self.upper is not None and self.lower > self.upper:
            raise exceptions.ParameterValueError(key=self.url_key, value=self.url_value,
                                                 message="Invalid bound range")

    def serialise(self):
        if self.lower or self.upper:
            return {self.url_key: {"gte": self.lower, "lte": self.upper}}
        return {}


class Boolean(BaseFilter):

    def __init__(self, *args, **kwargs):
        super(Boolean, self).__init__(*args, **kwargs)
        self.parsed_val = None,
        self.include_if_false = kwargs['include_if_false']

    def _parse(self):
        """Update parsed params with boolean arg value."""

        if not self.url_value:
            return

        self.parsed_val = self.parse_boolean()

    def _validate(self):
        pass

    def serialise(self):

        if self.parsed_val or self.include_if_false:
            return {self.url_key: self.parsed_val}

        return {}

    def parse_boolean(self):
        """Parse boolean argument types

        Returns True or False if argument is present, otherwise None."""

        arg_param = self.url_value
        if not arg_param:
            return None

        arg_check_int = re.search("^[0-1]$", arg_param)
        arg_check_bool = re.search("^true|false", arg_param.lower())
        if arg_check_int:
            return bool(int(arg_param))
        elif arg_check_bool:
            return {"true": True, "false": False}[arg_param.lower()]
        else:
            raise exceptions.ParameterValueError(key=self.url_value, value=arg_param)



