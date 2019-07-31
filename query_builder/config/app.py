from query_builder.app.filter_types import BooleanType,Collection,DateRange,NumericRange

class AppSettings(object):

    def __init__(self):
        self.DEBUG = True
        self.AUTO_RELOAD = True
        self.PORT = 3031

        self.SECTOR_ES_FIELD = 'sector.id'

        # self.COMPANIES_FILTERS = [
        #     "revenue", --
        #     "sector_context", --
        #     "ecommerce", --
        #     "limit", //
        #     "offset", //
        #     "cid", --
        #     "exclude_tps",//
        #     "cash", --
        #     "aggregate", --
        #     "trading_activity",
        # ]

        # self.COMPANIES_FILTERS = [
        #     {'type': NumericRange, 'argument': 'revenue', 'additionarguments': {}},
        #     {'type': NumericRange, 'argument': 'assets', 'additionarguments': {}},
        #     {'type': NumericRange, 'argument': 'cash', 'additionarguments': {}},
        #     {'type': Collection, 'argument': 'sector_context', 'additionarguments': {}},
        #     {'type': Collection, 'argument': 'cid', 'additionarguments': {}},
        #     {'type': BooleanType, 'argument': 'ecommerce', 'additionarguments': {'include_if_false': False}},
        #     {'type': BooleanType, 'argument': 'aggregate', 'additionarguments': {'include_if_false': False}},
        #     {'type': BooleanType, 'argument': 'exclude_tps', 'additionarguments': {'include_if_false': True}},
        #     {'type': DateRange, 'argument': 'trading_activity', 'additionarguments': {}}
        # ]

        self.COMPANIES_FILTERS = {
            'revenue': (NumericRange, {}),
            'assets': (NumericRange, {}),
            'cash': (NumericRange, {}),
            'sector_context': (Collection, {}),
            'cid': (Collection, {}),
            'ecommerce': (BooleanType, {'include_if_false' : False}),
            'aggregate': (BooleanType, {'include_if_false' : False}),
            'exclude_tps': (BooleanType, {'include_if_false': True}),
            'trading_activity': (DateRange, {})
        }
        self.app_settings = dict()
        self.app_settings["version"] = "2.19"

        # High level constants
        self.app_settings["results_limit_default"] = 500
        self.app_settings["page_size_default"] = 50


settings = AppSettings()
