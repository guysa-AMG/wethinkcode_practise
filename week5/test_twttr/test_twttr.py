import sys
from twttr import shorten

def correct(word):
    vowels = ["a","e","i","o","u"]
    return "".join([char for char in word if not char.lower() in vowels])

def test_run():
   
    testc=["Hello","Twitter:","Everyone","Heat?","CS50Python."]
    for test in testc:
        assert correct(test) == shorten(test)
            

def test_puctuation():
    test_list=["Hello?","Friends."]
    for words in test_list:
        assert correct(words) == shorten(words)


