import re
from query_builder import exceptions
from query_builder.app.handlers.base_filter import BaseFilter


class Dates(BaseFilter):

    def __init__(self, key, value, *args, **kwargs):
        super(NumericRange, self).__init__(key, value)


