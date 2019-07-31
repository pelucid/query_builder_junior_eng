from query_builder.exceptions import ParameterValueError

import pytest

from query_builder.app.filter_types.date_range import DateRange


@pytest.mark.parametrize('input, expected_lower, expected_upper', [
    (['20150101-20160101'], '2015-01-01', '2016-01-01'),
    (['-20160101'], None, '2016-01-01'),
    (['20150101-'], '2015-01-01', None)
])
def test_date_range(input, expected_lower, expected_upper):
    filter = DateRange('dummy_url_key', input)
    filter.parse_and_validate()
    assert filter.lower == expected_lower
    assert filter.upper == expected_upper


def test_raised_output_validation_error():
    with pytest.raises(ParameterValueError) as e:
        input = ['20160101-20150101']
        filter = DateRange('dummy', input)
        filter.parse_and_validate()
    assert e.value.message == u'Value Error for key \'dummy\': 20160101-20150101'
