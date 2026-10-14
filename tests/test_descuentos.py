
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
    descuento_apilado,
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



# PRUEBA 9: Descuentos apilados normales
def test_descuento_apilado_normal():
    # Arrange
    precio = 100000
    descuentos = [10, 20]
    esperado = 70000

    # Act
    resultado = descuento_apilado(precio, descuentos)

    # Assert
    assert resultado == pytest.approx(esperado)


# PRUEBA 10: Descuentos apilados superiores al 100 %
def test_descuento_apilado_supera_cien():
    # Arrange
    precio = 100000
    descuentos = [50, 60]
    esperado = 0

    # Act
    resultado = descuento_apilado(precio, descuentos)

    # Assert
    assert resultado == pytest.approx(esperado)


# PRUEBA 11: Descuentos apilados vacíos
def test_descuento_apilado_vacio():
    # Arrange
    precio = 100000
    descuentos = []
    esperado = 100000

    # Act
    resultado = descuento_apilado(precio, descuentos)

    # Assert
    assert resultado == esperado


# PRUEBA 12: Precio negativo en aplicar descuento
def test_aplicar_descuento_precio_negativo():
    # Arrange
    precio = -100
    porcentaje = 10

    # Act + Assert
    with pytest.raises(ValueError):
        aplicar_descuento(precio, porcentaje)


# PRUEBA 13: Precio negativo en calcular descuento
def test_calcular_descuento_precio_negativo():
    # Arrange
    precio = -200
    porcentaje = 20

    # Act + Assert
    with pytest.raises(ValueError):
        calcular_descuento(precio, porcentaje)


# PRUEBA 14: Porcentaje negativo en calcular descuento
def test_calcular_descuento_porcentaje_negativo():
    # Arrange
    precio = 100
    porcentaje = -10

    # Act + Assert
    with pytest.raises(ValueError):
        calcular_descuento(precio, porcentaje)


# PRUEBA 15: Precio negativo en precio final
def test_precio_final_precio_negativo():
    # Arrange
    precio = -100
    impuesto = 19
    descuento = 10

    # Act + Assert
    with pytest.raises(ValueError):
        calcular_precio_final(precio, impuesto, descuento)


# PRUEBA 16: Impuesto negativo
def test_precio_final_impuesto_negativo():
    # Arrange
    precio = 100
    impuesto = -19
    descuento = 10

    # Act + Assert
    with pytest.raises(ValueError):
        calcular_precio_final(precio, impuesto, descuento)


# PRUEBA 17: Descuento superior al 100%
def test_precio_final_descuento_invalido():
    # Arrange
    precio = 100
    impuesto = 19
    descuento = 120

    # Act + Assert
    with pytest.raises(ValueError):
        calcular_precio_final(precio, impuesto, descuento)


# PRUEBA 18: Volumen de 10 unidades
def test_descuento_volumen_10_unidades():
    # Arrange
    cantidad = 10
    precio_unitario = 1000
    esperado = 9500

    # Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)

    # Assert
    assert resultado == pytest.approx(esperado)


# PRUEBA 19: Volumen de 50 unidades
def test_descuento_volumen_50_unidades():
    # Arrange
    cantidad = 50
    precio_unitario = 1000
    esperado = 42500

    # Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)

    # Assert
    assert resultado == pytest.approx(esperado)


# PRUEBA 20: Volumen sin descuento
def test_descuento_volumen_5_unidades():
    # Arrange
    cantidad = 5
    precio_unitario = 1000
    esperado = 5000

    # Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)

    # Assert
    assert resultado == pytest.approx(esperado)


# PRUEBA 21: Cantidad negativa
def test_descuento_volumen_cantidad_negativa():
    # Arrange
    cantidad = -5
    precio_unitario = 1000

    # Act + Assert
    with pytest.raises(ValueError):
        descuento_por_volumen(cantidad, precio_unitario)


# PRUEBA 22: Precio unitario negativo
def test_descuento_volumen_precio_negativo():
    # Arrange
    cantidad = 20
    precio_unitario = -1000

    # Act + Assert
    with pytest.raises(ValueError):
        descuento_por_volumen(cantidad, precio_unitario)


# PRUEBA 23: Descuento acumulativo inválido
def test_descuento_acumulativo_invalido():
    # Arrange
    precio = 100000
    descuentos = [10, 120]

    # Act + Assert
    with pytest.raises(ValueError):
        descuento_cumulativo(precio, descuentos)
