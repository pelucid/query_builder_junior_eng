import pytest

from query_builder.app.handlers.filter_types import Boolean


@pytest.mark.parametrize('input, boolean', [
    ('1', True),
    ('true', True),
    ('TRUE', True),
    ('0', False),
    ('false', False),
    ('False', False),

])
def test_boolean_parse(input, boolean):
    filter = Boolean('dummy_url_key', input)
    filter._parse()
    assert filter.boolean is boolean



# TODO Test Failure Cases

# def test_boolean_parse_raises_exception():

# test for validate - not required as not implemented

# test for serialise

