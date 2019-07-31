"""ES querying layer."""


import datetime
import json
import glogging
import os


from query_builder.config.app import settings
from query_builder import __file__ as api_path
from query_builder.app.elastic import companies_search

api_version = settings.app_settings["version"]


class Piston(object):
    """Logic for converting parameter dictionaries into Elasticsearch Query"""

    def __init__(self, logger=None):
        api_directory = os.path.join(os.path.dirname(os.path.abspath(api_path)), 'logs')
        if logger:
            self.log = logger
        else:
            self.log = glogging.GLogging(logname='query_builder.piston', logdir=api_directory, log_to_screen=False)
            self.log.setLevel("DEBUG")

        self.queries_log = glogging.GLogging(logname="query_builder.piston.queries", logdir=api_directory, log_to_screen=False)
        self.queries_log.setLevel("DEBUG")

        self.dthandler = (lambda obj: obj.isoformat()
                            if isinstance(obj, datetime.datetime) or
                               isinstance(obj, datetime.date)
                            else None)

    def _log_query(self, query):
        """Write ES query to log file.

        Args:
            query: ES query as a python dict
        """
        self.queries_log.debug("doc_type: {0}, query: {1}".format("company", json.dumps(query, default=self.dthandler)))

    def company_search(self, params):
        """Search for companies by any parameter.

        Arguments:
            params: dictionary of params.
        Returns:
            list of _source documents returned by ES.
        """
        # Build the query from the params
        es_query = companies_search.query_builder(params)
        self._log_query(es_query)

        return es_query
