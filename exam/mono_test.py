from mono import monotonic
import pytest

def test_1():
    data = [(1,3,2),(1,2)]
    out = ['neither', 'monotonically increasing']
    assert monotonic(data) == out

def test_several():
    data = [(4, 3, 10, 1), (1, 2, 3.5), (4, 3.2, 1, -100), (1, 3.5, 1000, 1000.1)]
    out = ['neither', 'monotonically increasing', 'monotonically decreasing', 'monotonically increasing']

    assert monotonic(data) == out


