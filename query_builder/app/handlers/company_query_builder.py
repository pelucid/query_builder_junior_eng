import re
import urlparse

from query_builder import exceptions
from query_builder.app.elastic.piston import Piston
from query_builder.app.handlers.pagination import Pagination
from query_builder.config.app import settings
from query_builder.app.handlers.numeric_range_filter import NumericRange
from query_builder.app.handlers.boolean_filter import Boolean
from query_builder.app.handlers.dates_filter import Dates



FILTER_MAP = {
    'cash': NumericRange,
    'revenue': NumericRange,
    'exclude_tps': Boolean,
    'ecommerce': Boolean,
    'aggregate': Boolean,
    'trading_activity': Dates
    # 'cid': __,
    # 'cids': __,
    # 'sector_context': ___,
    # 'sectors': ___
}


class CompanyQueryBuilder(object):
    """Company Query Builder main handler."""

    def __init__(self, url):
        parsed_url = urlparse.urlparse(url)
        self.query_params = urlparse.parse_qs(parsed_url.query)
        self.valid_args = settings.COMPANIES_FILTERS
        self.piston = Piston()
        self.parsed_params = dict()

    def get(self):
        """Handle get requests to /company_query_builder"""
        self.pagination = Pagination(limit=self.get_argument("limit", None),
                                     offset=self.get_argument("offset", 0))

        self.validate_args(self.valid_args)
        self.parse_parameters()
        self.parsed_params["size"] = self.pagination.page_size
        self.parsed_params["from"] = self.pagination.page_offset
        es_query = self.piston.company_search(self.parsed_params)

        return es_query

    def get_argument(self, name, default=None):
        return self.query_params.get(name, [default])[-1]

    def get_arguments(self, name):
        return self.query_params.get(name, [])

    def validate_args(self, valid_arguments=None, required_args=None):
        """Check argument parameters are valid and present raise exception if not"""
        request_set = set(self.query_params.keys())
        if valid_arguments:
            invalid = request_set - set(valid_arguments)
            if invalid:
                raise exceptions.ParameterKeyError(key=", ".join(invalid))

        if required_args:
            missing = set(required_args) - request_set
            if missing:
                raise exceptions.ParameterKeyError(key=", ".join(missing))

    def parse_parameters(self, org=None, model_config=None):
        """Parse the URL parameters and build parsed_params dict."""

        # TODO (COMPLETE REFACTOR)
        for param_key in settings.COMPANIES_FILTERS:
            param_value = self.get_argument(param_key)
            filter_ = FILTER_MAP.get(param_key, None)
            if filter_ is not None:
                f = filter_(param_key, param_value)
                f.parse_and_validate()
                serialised_filter = f.serialise()
                self.parsed_params.update(serialised_filter)


        # Args which may have multiple queries e.g. &cid=1&cid=2
        self.parse_get_arguments("cid", "cids")
        self.parse_get_arguments("sector_context", "sectors")



    def parse_get_arguments(self, arg, key=None):
        """Update parsed params if arg in request"""
        key = key or arg
        args = self.get_arguments(arg)
        if args:
            self.add_to_parsed_params(key, args)


    def add_to_parsed_params(self, param_key, param_value):
        """Add params to parsed_params if arg exists"""
        self.parsed_params[param_key] = param_value
