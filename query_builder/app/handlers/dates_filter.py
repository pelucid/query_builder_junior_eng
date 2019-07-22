import datetime
from query_builder import exceptions
from query_builder.app.handlers.base_filter import BaseFilter


class Dates(BaseFilter):
    def __init__(self, *args, **kwargs):
        super(Dates, self).__init__(*args, **kwargs)
        self.datefrom = None
        self.dateto = None


    def parse_date(self, arg):
        """ Parse a date argument """

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

        self.datefrom, self.dateto = self.url_value.split('-')
        self.datefrom = self.parse_date(self.datefrom)
        self.dateto = self.parse_date(self.dateto)


    def _validate(self):
        pass

    def serialise(self):
        if self.datefrom or self.dateto:
            output_dict = {}
            output_dict[self.url_key] = dict()
            if self.datefrom:
                output_dict[self.url_key]["gte"] = self.datefrom
            if self.dateto:
                output_dict[self.url_key]["lte"] = self.dateto
            return output_dict