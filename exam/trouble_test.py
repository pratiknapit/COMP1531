'''
Tests
'''
from trouble import clear, flip_card, is_double_trouble, is_trouble_double, is_empty

def test_simple():
    clear()
    flip_card({
        'suit': 'Hearts',
        'number': '9',
    })
    flip_card({
        'suit': 'Clubs',
        'number': '9',
    })
    assert not is_trouble_double()
    assert not is_empty()
    assert is_double_trouble()

# Write your tests here

def test_flip_card():
    clear()
    flip_card({
        'suit': 'Hearts',
        'number': '9',
    })
    flip_card({
        'suit': 'Clubs',
        'number': '9',
    })
    flip_card({
        'suit': 'Clubs',
        'number': '9',
    })

    assert flip_card({
        'suit': 'Clubs',
        'number': '10',
    }) == {}

    assert is_empty() == False

def test_double_trouble():
    clear()
    flip_card({
        'suit': 'Hearts',
        'number': '9',
    })
    assert is_double_trouble() == False

    flip_card({
        'suit': 'Clubs',
        'number': '9',
    })

    assert is_double_trouble() == True
    assert is_empty() == True

def test_double_trouble_false():
    clear()
    flip_card({
        'suit': 'Hearts',
        'number': '9',
    })
    assert is_double_trouble() == False

    flip_card({
        'suit': 'Clubs',
        'number': '9',
    })

    flip_card({
        'suit': 'Clubs',
        'number': '10',
    })


    assert is_double_trouble() == False
    assert is_empty() == False

def test_trouble_double():
    clear()
    flip_card({
        'suit': 'Hearts',
        'number': '9',
    })

    flip_card({
        'suit': 'Hearts',
        'number': '10',
    })

    assert is_trouble_double() == False

    flip_card({
        'suit': 'Hearts',
        'number': '2',
    })

    flip_card({
        'suit': 'Hearts',
        'number': '3',
    })

    assert is_trouble_double() == True
    assert is_empty() == True




def test_trouble_false():
    clear()
    flip_card({
        'suit': 'Hearts',
        'number': '9',
    })

    flip_card({
        'suit': 'Hearts',
        'number': '10',
    })

    assert is_trouble_double() == False

    flip_card({
        'suit': 'Hearts',
        'number': '2',
    })

    flip_card({
        'suit': 'Hearts',
        'number': '3',
    })

    flip_card({
        'suit': 'Diamonds',
        'number': '3',
    })

    assert is_trouble_double() == False

    assert is_empty() == False


def test_empty_clear():

    assert clear() == {}

    assert is_empty() == True

