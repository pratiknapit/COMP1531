from acronym import acronym_make

def test_1():
    assert acronym_make(['I am very tired today']) == ['VTT']

def test_2():
    assert acronym_make(['Why didnt I study for this exam more', 'I dont know']) == ['WDSFTM', 'DK']
