import pytest

from query_builder.app.handlers.base_filter import Boolean


@pytest.mark.parametrize('input, expected_positive, expected_negative', [
    ('true', True, None),
    ('True', True, None),
    ('TRUE', True, None),
    ('1', True, None),
    ('false', None, False),
    ('False', None, False),
    ('FALSE', None, False),
    ('0', None, False)
])

def test_boolean(input, expected_positive, expected_negative):
    filter = Boolean('dummy_url_key', input)
    filter.parse_and_validate()
    assert filter.positive == True
    assert filter.negative == False