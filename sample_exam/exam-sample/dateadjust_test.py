from dateadjust import adjust

import pytest

def test_1():
    assert adjust(4, 4, '16:40 on 28 January 2021') == '20:40 on 25 February 2021'


def test_2():
    assert adjust(0, -2, '14:00 on 2 January 2020') == '12:00 on 2 January 2020' 

def test_3():
    assert adjust(5, 4, '12:00 on 2 January 2021') == '16:00 on 6 February 2021'

def test_error():
    with pytest.raises(ValueError):
        assert adjust(55, 4, '12:00 on 2 January 2021') 
