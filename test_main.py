from main import add, asdf, subtract, multiply

def test_add():
    assert add(1, 2) == 3

def test_subtract():
    assert subtract(2, 1) == 1

def test_multiply():
    assert multiply(2, 3) == 6

def test_asdf():
    assert asdf(0) == "rip"
