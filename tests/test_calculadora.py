import pytest

from src.calculadora import sumar, raiz_cuadrada, minimo


# PRUEBA 1: Verificar una suma correcta
def test_sumar_numeros_positivos():
    # Arrange
    a = 7
    b = 5
    esperado = 12

    # Act
    resultado = sumar(a, b)

    # Assert
    assert resultado == esperado


# PRUEBA 2: Detectar el bug de raíz cuadrada
def test_raiz_cuadrada_negativa_lanza_error():
    # Arrange
    numero = -4

    # Act + Assert
    with pytest.raises(ValueError):
        raiz_cuadrada(numero)


# PRUEBA 3: Detectar el bug del mínimo
def test_minimo_lista_positivos():
    # Arrange
    numeros = [5, 8, 3]
    esperado = 3

    # Act
    resultado = minimo(numeros)

    # Assert
    assert resultado == esperado
