from query_builder.app.handlers.base_filter import BaseFilter

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
            raise exceptions.ParameterValueError(
                key=self.url_key, value=self.url_value)

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
            raise exceptions.ParameterValueError(
                key=self.url_key, value=self.url_value)

    def _validate(self):
        """Validate Lower is not greater than Upper"""
        if self.lower is not None and self.upper is not None and self.lower > self.upper:
            raise exceptions.ParameterValueError(
                key=self.url_key, value=self.url_value)

    def serialise(self):
        if self.lower or self.upper:
            return {self.url_key: {"gte": self.lower, "lte": self.upper}}
        return {}
