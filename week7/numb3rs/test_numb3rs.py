import re
from numb3rs import validate

def tvalidate(addr):
    val =  re.match(r"^((25[0-5]|2[0-4]\d|1\d\d|\d{1,2})\.){3}(25[0-5]|2[0-4]\d|1\d\d|\d{1,2})$",addr)
    if val:
        return True
    else:
        return False

def test_validate():
    tests=["192.168.2.1","255.255.255.255","10.-1.0.1","000.001.010.100","255.0.0.256"]
    for test in tests:
        assert validate(test) == tvalidate(test)
def test_invalid_input():
    tests=[" ",".","hello","255255255"]
    for test in tests:
        assert validate(test) == False

def test_invalid_length():
    tests=["192","192.168.43.56.349","192.168","255.255.255"]
    for test in tests:
        assert validate(test) == False



