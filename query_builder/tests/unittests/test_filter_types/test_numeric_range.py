import pytest

from query_builder.exceptions import ParameterValueError
from query_builder.app.handlers.numeric_range_filter import NumericRange
#  Add additional unit tests to NumericRange to test the validation error
#  or parse error cases


@pytest.mark.parametrize('input, expected_lower, expected_upper', [
    ('100-2000', 100, 2000),
    ('-10-2000', -10, 2000),
    ('-2000', None, 2000),
    ('1231234-', 1231234, None)
])
def test_numeric_range(input, expected_lower, expected_upper):
    filter = NumericRange('dummy_url_key', input)
    filter.parse_and_validate()
    assert filter.lower == expected_lower
    assert filter.upper == expected_upper

@pytest.mark.parametrize('input', [
    ('a-b'),
    ('1e6-10e6')
])
def test_raises_exception_if_input_outside_range(input):
    filter = NumericRange('dummy_url_key', input)
    with pytest.raises(ParameterValueError) as e_info:
        filter.parse_and_validate()

