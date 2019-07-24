import pytest

from query_builder.app.handlers.filter_types import NumericRange
from query_builder.exceptions import ParameterValueError


@pytest.mark.parametrize('input, expected_lower, expected_upper', [
    ('100-2000', 100, 2000),
    ('-10-2000', -10, 2000),
    ('-2000', None, 2000),
    ('-', None, None),
    ('0-0', 0, 0),
    ('1231234-', 1231234, None)

])
def test_numeric_range(input, expected_lower, expected_upper):
    filter = NumericRange('dummy_url_key', input)
    filter.parse_and_validate()
    assert filter.lower == expected_lower
    assert filter.upper == expected_upper


@pytest.mark.parametrize('input, e', [
    ('100-?200', "Does not match expected format"),
    ('100 200', "Does not match expected format"),
    ('10-2', "Invalid bound range"),
    ('0-hi', "Cannot convert value to int"),
    ('hi-5', "Cannot convert value to int"),
    ('hi-hi', "Cannot convert value to int"),


])
def test_numeric_range_failure_cases(input, e):
    filter = NumericRange('dummy_url_key', input)

    with pytest.raises(ParameterValueError) as e_info:
        filter.parse_and_validate()

        assert e_info.message == e

