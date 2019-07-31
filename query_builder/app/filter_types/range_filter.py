from base_filter import BaseFilter
from query_builder.exceptions import ParameterValueError
from datetime import datetime


class RangeFilter(BaseFilter):
    def __init__(self, *args, **kwargs):
        super(RangeFilter, self).__init__(*args, **kwargs)
        self.lower = None
        self.upper = None

    def _parse(self):
        raise NotImplementedError

    def _validate(self):
        """Validate Lower is not greater than Upper"""

        if self.lower is not None and self.upper is not None and self.lower > self.upper:
            raise ParameterValueError(key=self.url_key, value=self.url_value)

    def serialise(self):
        if self.lower or self.upper:
            return {self.url_key: {"gte": self.lower, "lte": self.upper}}
        return {}