
"""
Pruebas unitarias del módulo descuentos.
Metodología AAA: Arrange, Act, Assert.
"""

import pytest

from src.descuentos import (
    aplicar_descuento,
    calcular_descuento,
    calcular_precio_final,
    descuento_por_volumen,
    descuento_cumulativo,
)


# PRUEBA 1: Aplicación de descuento normal
def test_aplicar_descuento_normal():
    # Arrange
    precio = 100000
    porcentaje = 10
    esperado = 90000

    # Act
    resultado = aplicar_descuento(precio, porcentaje)

    # Assert
    assert resultado == pytest.approx(esperado)


# PRUEBA 2: Descuento fuera de rango
def test_aplicar_descuento_mayor_a_cien():
    # Arrange
    precio = 100000
    porcentaje = 120

    # Act + Assert
    with pytest.raises(ValueError):
        aplicar_descuento(precio, porcentaje)


# PRUEBA 3: Calcular el monto descontado
def test_calcular_descuento():
    # Arrange
    precio = 200000
    porcentaje = 20
    esperado = 40000

    # Act
    resultado = calcular_descuento(precio, porcentaje)

    # Assert
    assert resultado == pytest.approx(esperado)


# PRUEBA 4: Detectar el bug del impuesto
def test_precio_final_aplica_impuesto_despues_descuento():
    # Arrange
    precio = 100000
    impuesto = 19
    descuento = 10
    esperado = 107100

    # Act
    resultado = calcular_precio_final(
        precio, impuesto, descuento
    )

    # Assert
    assert resultado == pytest.approx(esperado)


# PRUEBA 5: Descuento por volumen de 20 unidades
def test_descuento_volumen_20_unidades():
    # Arrange
    cantidad = 20
    precio_unitario = 1000
    esperado = 18000

    # Act
    resultado = descuento_por_volumen(
        cantidad, precio_unitario
    )

    # Assert
    assert resultado == pytest.approx(esperado)


# PRUEBA 6: Descuento por volumen de 100 unidades
def test_descuento_volumen_100_unidades():
    # Arrange
    cantidad = 100
    precio_unitario = 1000
    esperado = 80000

    # Act
    resultado = descuento_por_volumen(
        cantidad, precio_unitario
    )

    # Assert
    assert resultado == pytest.approx(esperado)


# PRUEBA 7: Descuentos acumulativos
def test_descuentos_acumulativos():
    # Arrange
    precio = 100000
    descuentos = [10, 20]
    esperado = 72000

    # Act
    resultado = descuento_cumulativo(
        precio, descuentos
    )

    # Assert
    assert resultado == pytest.approx(esperado)


# PRUEBA 8: Descuento acumulativo vacío
def test_descuentos_acumulativos_vacios():
    # Arrange
    precio = 50000
    descuentos = []
    esperado = 50000

    # Act
    resultado = descuento_cumulativo(
        precio, descuentos
    )

    # Assert
    assert resultado == esperado

