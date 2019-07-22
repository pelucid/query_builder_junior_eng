import pytest

from query_builder.app.handlers.base_filter import NumericRange
#  Add additional unit tests to NumericRange to test the validation error
#  or parse error cases

#   def _parse(self):
#         raise NotImplementedError

#     def _validate(self):
#         raise NotImplementedError


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


# TODO Test Failure Cases


# validation error
def test_raises_exception_if_input_outside_range(input, expected_lower, expected_upper):


filter = NumericRange('dummy_url_key', input)
filter.parse_and_validate()
# filter.lower < expected_lower
# filter.upper > expected_upper
if not isinstance(filter.lower == expected_lower)
if not isinstance(filter.upper == expected_upper)
raise AssertionError('The value must be within the given range')


# parse error
def test_raises_exception_if_input_not_integer(input)


filter = NumericRange('dummy_url_key', input)
filter.parse_and_validate()
if not isinstance(input, int)
raise TypeError('The value entered must be a number')
