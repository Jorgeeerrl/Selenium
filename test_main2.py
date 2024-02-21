from pytest import mark

@mark.api
@mark.data
def test_prueba01():
    assert True

@mark.parametrize('nombre',['Jorge','Neo','Enzo'])
def test_prueba02(nombre):
    assert True
    print("Valor parámetro= " + nombre)

@mark.ui
def test_prueba03():
    assert True