import datetime

from numeric_range import NumericRange
from query_builder import exceptions
from query_builder.exceptions import ParameterValueError


class DateRange(NumericRange):
    def __init__(self, *args, **kwargs):
        super(DateRange, self).__init__(*args, **kwargs)

    def parse_date(self, arg):
        if arg:
            try:
                parameter = datetime.datetime.strptime(
                    arg, '%Y%m%d').date().isoformat()
                return parameter
            except Exception as e:
                raise exceptions.ParameterValueError(key=arg, value=arg,
                                                     message=e.message)

    def _parse(self):
        """Parse the dates arguments from URL params."""
        datefrom, dateto = self.url_value.split('-')

        self.lower = self.parse_date(datefrom)
        self.upper = self.parse_date(dateto)

    def _validate(self):
        """validate the date arguments from URL params."""

        lowerdate = None
        upperdate = None

        if self.lower is not None:
            lowerdate = datetime.datetime.strptime(self.lower, '%Y-%m-%d')

        if self.upper is not None:
            upperdate = datetime.datetime.strptime(self.upper, '%Y-%m-%d')

        if lowerdate is not None and upperdate is not None and lowerdate > upperdate:
            raise ParameterValueError(key=self.url_key, value=self.url_value)