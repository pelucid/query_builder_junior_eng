import re
import exceptions


class BaseFilter(object):
    def __init__(self, url_key, url_value):
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




"""
class Boolean(BaseFilter)


class Dates(BaseFilter)


"""
