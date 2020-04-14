import graphene

from temperature import schema


def test_query():
    """Test that everything is plumbed together and has the right names.

    Not testing the implementation or network layer
    """
    s = graphene.Schema(query=schema.Query)
    result = s.execute('query { currentTemperature{ timestamp value unit}}')
    assert {'timestamp', 'value', 'unit'} == set(result.data['currentTemperature'].keys())


def test_subscription():
    # Todo (Rishi): figure out how one tests subscriptions. The Graphene test client docs aren't helping here.
    pass
