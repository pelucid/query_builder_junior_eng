import pytest

from query_builder.app.handlers.filter_types import NumericRange, Boolean
from query_builder.exceptions import ParameterValueError


@pytest.mark.parametrize('input, expected_bool', [
    ('FALSE', False),
    ('False', False),
    ('false', False),
    ('0', False),
    ('TRUE', True),
    ('True', True),
    ('true', True),
    ('1', True),

])
def test_boolean(input, expected_bool):
    filter = Boolean('dummy_url_key', input)
    filter.parse_and_validate()

    assert filter.parsed_val == expected_bool


@pytest.mark.parametrize('input', [
    '42',
    'fasle',
    'fasle42',
    ' false',
    'no',
])
def test_boolean_failure_cases(input):
    filter = Boolean('dummy_url_key', input)

    with pytest.raises(ParameterValueError):
        filter.parse_and_validate()




