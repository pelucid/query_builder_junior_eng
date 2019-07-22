import pytest

from app.handlers.boolean_filter import Boolean
from query_builder.exceptions import ParameterValueError


@pytest.mark.parametrize('input, expected', [
    ('true', True),
    ('TRUE', True),
    ('1', True),
    ('false', False),
    ('FALSE', False),
    ('0', False)
])
def test_boolean(input, expected):
    filter = Boolean('dummy_url_key', input)
    filter.parse_and_validate()
    assert filter.bool_val == expected

@pytest.mark.parametrize('input', [
    ('123'),
    ('test'),
])
def test_raises_exception_if_input_incorrect(input):
    filter = Boolean('dummy_url_key', input)
    with pytest.raises(ParameterValueError) as e_info:
        filter.parse_and_validate()