from flask import Flask
from flask import request
from flask import jsonify

from query_builder.config.app import settings
from query_builder.app.handlers import company_query_builder

application = Flask(__name__)


@application.route('/v1/company_query_builder', methods=['GET'])
def hello():
    es_query = get_es_query(request.full_path)
    return jsonify(es_query)


def get_es_query(request_url):
    """
    Given a request URL path with query parameters, return an elasticsearch query
    Args:
        request_url: path with query parameters, string

    Returns:
        Dictionary - elasticsearch query
    """
    handler = company_query_builder.CompanyQueryBuilder(request_url)
    return handler.get()


if __name__ == "__main__":
    application.run(port=settings.PORT, debug=settings.DEBUG, use_reloader=settings.AUTO_RELOAD)