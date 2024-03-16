from penguin import validate

def test_1():
    assert validate('P8464Q94944Z')

def test_2():
    assert validate('A1234B12344C')

def test_3():
    assert not validate('A1234567890B')

def test_others_false():

    assert not validate('51234567890B')

def test_fail1():

    assert not validate('a1234567890B')

def test_fail2():
    assert not validate('A1234a67890B')

def test_fail3():
    assert not validate('A1234567890b')

def test_fail4():
    assert not validate('A1234567890bdfsf')

def test_fail5():
    assert not validate('P8464Q94945Z')




