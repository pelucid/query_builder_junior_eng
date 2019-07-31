import pytest

from query_builder.app.filter_types import Collection


@pytest.mark.parametrize('key, values', [
    ('cid', ['1','2','3','4']),
    ('cid', ['1','1','1']),
    ('cid', ['1'])
])

def test_multiple_collection_results(key, values):
    c = Collection(key, values)
    c.parse_and_validate()
    output = c.serialise()
    assert output == {key: values}