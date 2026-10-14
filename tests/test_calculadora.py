
"""
Pruebas unitarias del módulo calculadora.

Estructura AAA:
- Arrange: preparar datos.
- Act: ejecutar la función.
- Assert: verificar el resultado.
"""

import pytest

from src.calculadora import (
    sumar,
    restar,
    multiplicar,
    dividir,
    potencia,
    raiz_cuadrada,
    promedio,
    maximo,
    minimo,
    calcular_area_rectangulo,
    calcular_perimetro_rectangulo,
)


# PRUEBA 1: Suma de números positivos
def test_sumar_numeros_positivos():
    # Arrange
    a, b = 7, 5
    esperado = 12

    # Act
    resultado = sumar(a, b)

    # Assert
    assert resultado == esperado


# PRUEBA 2: Raíz cuadrada de número negativo
def test_raiz_cuadrada_negativa_lanza_error():
    # Arrange
    numero = -4

    # Act + Assert
    with pytest.raises(ValueError):
        raiz_cuadrada(numero)


# PRUEBA 3: Mínimo de una lista positiva
def test_minimo_lista_positivos():
    # Arrange
    numeros = [5, 8, 3]
    esperado = 3

    # Act
    resultado = minimo(numeros)

    # Assert
    assert resultado == esperado


# PRUEBA 4: Resta con resultado negativo
def test_restar_resultado_negativo():
    # Arrange
    a, b = 10, 15
    esperado = -5

    # Act
    resultado = restar(a, b)

    # Assert
    assert resultado == esperado


# PRUEBA 5: Multiplicación con número negativo
def test_multiplicar_por_negativo():
    # Arrange
    a, b = -4, 3
    esperado = -12

    # Act
    resultado = multiplicar(a, b)

    # Assert
    assert resultado == esperado


# PRUEBA 6: División normal
def test_dividir_numeros_positivos():
    # Arrange
    a, b = 10, 2
    esperado = 5

    # Act
    resultado = dividir(a, b)

    # Assert
    assert resultado == esperado


# PRUEBA 7: División por cero
def test_dividir_por_cero_lanza_error():
    # Arrange
    a, b = 10, 0

    # Act + Assert
    with pytest.raises(ValueError):
        dividir(a, b)


# PRUEBA 8: Potencia con exponente positivo
def test_potencia_exponente_positivo():
    # Arrange
    base, exponente = 2, 3
    esperado = 8

    # Act
    resultado = potencia(base, exponente)

    # Assert
    assert resultado == esperado


# PRUEBA 9: Raíz cuadrada positiva
def test_raiz_cuadrada_positiva():
    # Arrange
    numero = 25
    esperado = 5

    # Act
    resultado = raiz_cuadrada(numero)

    # Assert
    assert resultado == esperado


# PRUEBA 10: Promedio de una lista
def test_promedio_lista_numeros():
    # Arrange
    numeros = [4, 6, 8]
    esperado = 6

    # Act
    resultado = promedio(numeros)

    # Assert
    assert resultado == esperado


# PRUEBA 11: Promedio de lista vacía
def test_promedio_lista_vacia_lanza_error():
    # Arrange
    numeros = []

    # Act + Assert
    with pytest.raises(ValueError):
        promedio(numeros)


# PRUEBA 12: Máximo de una lista
def test_maximo_lista_positivos():
    # Arrange
    numeros = [3, 9, 5]
    esperado = 9

    # Act
    resultado = maximo(numeros)

    # Assert
    assert resultado == esperado


# PRUEBA 13: Máximo de lista vacía
def test_maximo_lista_vacia_lanza_error():
    # Arrange
    numeros = []

    # Act + Assert
    with pytest.raises(ValueError):
        maximo(numeros)


# PRUEBA 14: Área de un rectángulo
def test_calcular_area_rectangulo():
    # Arrange
    base, altura = 5, 4
    esperado = 20

    # Act
    resultado = calcular_area_rectangulo(base, altura)

    # Assert
    assert resultado == esperado


# PRUEBA 15: Perímetro de un rectángulo
def test_calcular_perimetro_rectangulo():
    # Arrange
    base, altura = 5, 4
    esperado = 18

    # Act
    resultado = calcular_perimetro_rectangulo(base, altura)

    # Assert
    assert resultado == esperado

