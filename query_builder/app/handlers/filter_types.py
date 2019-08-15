import re
import exceptions


class BaseFilter(object):
    def __init__(self, url_key, url_value, **kwargs):
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
            raise exceptions.ParameterValueError(key=self.url_key, value=self.url_value)

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
            raise exceptions.ParameterValueError(key=self.url_key, value=self.url_value)

    def _validate(self):
        """Validate Lower is not greater than Upper"""
        if self.lower is not None and self.upper is not None and self.lower > self.upper:
            raise exceptions.ParameterValueError(key=self.url_key, value=self.url_value)

    def serialise(self):
        if self.lower or self.upper:
            return {self.url_key: {"gte": self.lower, "lte": self.upper}}
        return {}


class Boolean(BaseFilter):
    def __init__(self, *args, **kwargs):
        super(Boolean, self).__init__(*args, **kwargs)
        self.boolean = None
        self.include_if_false = kwargs.get('include_if_false', True)

    def _parse(self):

        if not self.url_value:
            return

        arg_check_int = re.search("^[0-1]$", self.url_value)
        arg_check_bool = re.search("^true|false", self.url_value.lower())
        if arg_check_int:
            self.boolean = bool(int(self.url_value))
        elif arg_check_bool:
            self.boolean = {"true": True, "false": False}[self.url_value.lower()]
        else:
            raise exceptions.ParameterValueError(key=self.url_key, value=self.url_value)


    def _validate(self):
        """No validation needed"""
        pass

    def serialise(self):

        if self.boolean is None:
            return {}
        elif self.include_if_false is False and self.boolean is False:
            return {}
        else:
            return {self.url_key: self.boolean}