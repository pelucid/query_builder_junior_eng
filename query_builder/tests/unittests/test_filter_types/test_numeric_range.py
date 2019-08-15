import pytest

from query_builder.app.handlers.filter_types import NumericRange

@pytest.mark.parametrize('input, expected_lower, expected_upper', [
    ('100-2000', 100, 2000),
    ('-10-2000', -10, 2000),
    ('-2000', None, 2000),
    ('1231234-', 1231234, None),
    #test '-' only


])
def test_numeric_range(input, expected_lower, expected_upper):
    filter = NumericRange('dummy_url_key', input)
    filter.parse_and_validate()
    assert filter.lower == expected_lower
    assert filter.upper == expected_upper

# TODO Test Failure Cases

def test_numeric_range_parse_and_validate_raises_exception():
    input ='hello'
    filter = NumericRange('dummy_url_key', input)
    #would try with specific exception ParameterValueError
    with pytest.raises(Exception) as e:
        filter.parse_and_validate()
    assert e is not None
    #test exception message
    #test initial input throw exception

#test for parse

#test for validate

#test for serialise

#test for parse_match
