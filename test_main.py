from pytest import mark

@mark.ui  # Esto marca esta prueba
def test_prueba01():
    assert True

def test_prueba02():
    assert True

@mark.api
def test_prueba03():
    a=20
    assert a>=70