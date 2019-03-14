import pytest

from query_builder.app.handlers.filter_types import NumericRange


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
