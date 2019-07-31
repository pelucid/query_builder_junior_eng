from query_builder.exceptions import ParameterValueError

import pytest

from query_builder.app.filter_types import NumericRange


@pytest.mark.parametrize('input, expected_lower, expected_upper', [
    (['100-2000'], 100, 2000),
    (['-10-2000'], -10, 2000),
    (['-2000'], None, 2000),
    (['1231234-'], 1231234, None),
    (['-300--200'], -300, -200)  # Test double negatives
])
def test_numeric_range(input, expected_lower, expected_upper):
    filter = NumericRange('dummy_url_key', input)
    filter.parse_and_validate()
    assert filter.lower == expected_lower
    assert filter.upper == expected_upper


def test_raised_validation_error():
    with pytest.raises(ParameterValueError) as e:
        input = ['100-50']
        filter = NumericRange('dummy', input)
        filter.parse_and_validate()
    assert e.value.message == u'Value Error for key \'dummy\': 100-50'
