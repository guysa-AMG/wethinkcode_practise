from bank import value


def test_partial():
    assert value("How you doing?") == 20
    assert value("Howzit ") == 20
def test_full():
    assert value("Hello") == 0

def test_case():
    assert value("Morning") == 100

