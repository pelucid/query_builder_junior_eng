import pytest

from query_builder.app.filter_types import BooleanType

@pytest.mark.parametrize('input, includeiffalse, result', [
    (['true'], True, True),
    (['false'], True, False),
    (['false'], False , None)
])
def test_filter_if_false(input, includeiffalse, result):
    filter = BooleanType('dummy', input, include_if_false=includeiffalse)
    filter.parse_and_validate()
    output = filter.serialise()
    if output:
        assert output['dummy'] == result