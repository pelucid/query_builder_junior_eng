from base_filter import BaseFilter


class Collection(BaseFilter):
    def __init__(self, *args, **kwargs):
        super(Collection, self).__init__(*args, **kwargs)

    def get_url_value_from_arguments(self):
        pass

    def _parse(self):
        pass

    def _validate(self):
        pass

    def serialise(self):
        if self.url_value:
            return {self.url_key: self.url_value}
        return {}