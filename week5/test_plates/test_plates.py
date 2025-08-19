
from plates import is_valid
#check if the input is inbetween 2 to 6 characters
#check if the first two char is Alphabet
#make sure that the first number in the char in plate is not a 0
#make sure the numbers don't appear in the middle

def test_input_Length():
    assert is_valid("I") == False
    assert is_valid("Hello") == True
    assert is_valid("HMDB454") == False
def test_special_char():
    assert is_valid("Hello$") == False
    assert is_valid("%VIMGP") == False
    assert is_valid("GP452.") == False
def test_positioning():
    assert is_valid("LM45GP") == False
    assert is_valid("56HNPS") == False
def test_positioning2():
    assert is_valid("H94395") == False
    assert is_valid("123456") == False
    assert is_valid("GMK014") == False

def test_positive_cases():
    assert is_valid("HMV456") == True
    assert is_valid("GP") == True
    