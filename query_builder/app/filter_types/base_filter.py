class BaseFilter(object):
    def __init__(self, url_key, url_value, **kwargs):
        self.url_key = url_key
        self.url_value = url_value

        self.get_url_value_from_arguments()

    def get_url_value_from_arguments(self):
        self.url_value = self.url_value[-1]

    def parse_and_validate(self):
        self._parse()
        self._validate()

    def _parse(self):
        raise NotImplementedError

    def _validate(self):
        raise NotImplementedError

    def serialise(self):
        raise NotImplementedError