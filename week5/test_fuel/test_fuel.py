from fuel import convert,gauge


def test_gauge():
    
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert  gauge(50) == "50%"
   

def test_positive_convert():
    assert convert("1/4") == 25
    assert convert("1/2")== 50
    assert convert("3/4") == 75
    assert convert("1/1") == 100
    

def test_negative_convert():
    try:
        convert("-1/2")
    except ValueError:
        assert True
    else:
        assert False

    try:
        convert("-4/-9")
    except ValueError:
        assert True
    else:
        assert False
    
def test_incorrect_xory():
    try:
        convert("6/5")
    except ValueError:
        assert True
    else:
        assert False
    try:
        convert("2/0")
    except ZeroDivisionError:
        assert True
    else:
        assert False    
   
 
  