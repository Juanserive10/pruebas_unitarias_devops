"""
Pruebas unitarias del módulo csv_parser.

Metodología AAA: Arrange, Act, Assert.
Incluye pruebas de casos límite, detección de bugs
y mocking sin acceder al sistema de archivos.
"""

from unittest.mock import patch
import pytest

from src.csv_parser import (
    parse_csv_line,
    leer_csv_como_lista,
    csv_a_diccionarios,
    validar_csv,
    extraer_columna,
    filtrar_por_columna,
    contar_filas,
    contar_columnas,
)


# PRUEBA 1: CSV sencillo
def test_parse_csv_line_normal():
    # Arrange
    linea = "Juan,19,Manizales"
    esperado = ["Juan", "19", "Manizales"]

    # Act
    resultado = parse_csv_line(linea)

    # Assert
    assert resultado == esperado


# PRUEBA 2: Línea vacía
def test_parse_csv_line_vacia():
    # Arrange
    linea = []
    esperado = []

    # Act
    resultado = parse_csv_line(linea)

    # Assert
    assert resultado == esperado


# PRUEBA 3: Detectar bug de comillas y comas
def test_parse_csv_line_comillas_con_coma():
    # Arrange
    linea = 'Juan,"Manizales, Caldas",19'
    esperado = ["Juan", "Manizales, Caldas", "19"]

    # Act
    resultado = parse_csv_line(linea)

    # Assert
    assert resultado == esperado


# PRUEBA 4: Comillas escapadas
def test_parse_csv_line_comillas_escapadas():
    # Arrange
    linea = 'Juan,"Dijo ""Hola""",19'
    esperado = ["Juan", 'Dijo "Hola"', "19"]

    # Act
    resultado = parse_csv_line(linea)

    # Assert
    assert resultado == esperado


# PRUEBA 5: Convertir CSV a listas
def test_leer_csv_como_lista():
    # Arrange
    contenido = "nombre,edad\nJuan,19"
    esperado = [["nombre", "edad"], ["Juan", "19"]]

    # Act
    resultado = leer_csv_como_lista(contenido)

    # Assert
    assert resultado == esperado


# PRUEBA 6: Convertir CSV a diccionarios
def test_csv_a_diccionarios_normal():
    # Arrange
    contenido = "nombre,edad\nJuan,19"
    esperado = [{"nombre": "Juan", "edad": "19"}]

    # Act
    resultado = csv_a_diccionarios(contenido)

    # Assert
    assert resultado == esperado


# PRUEBA 7: Detectar bug de filas incompletas
def test_csv_a_diccionarios_fila_incompleta():
    # Arrange
    contenido = "nombre,edad,ciudad\nJuan,19"
    esperado = [{
        "nombre": "Juan",
        "edad": "19",
        "ciudad": ""
    }]

    # Act
    resultado = csv_a_diccionarios(contenido)

    # Assert
    assert resultado == esperado


# PRUEBA 8: Validar CSV correcto
def test_validar_csv_correcto():
    # Arrange
    contenido = "nombre,edad\nJuan,19"

    # Act
    resultado = validar_csv(contenido)

    # Assert
    assert resultado is True


# PRUEBA 9: Extraer columna
def test_extraer_columna():
    # Arrange
    contenido = "nombre,edad\nJuan,19\nAna,20"
    esperado = ["edad", "19", "20"]

    # Act
    resultado = extraer_columna(contenido, 1)

    # Assert
    assert resultado == esperado


# PRUEBA 10: Filtrar por columna
def test_filtrar_por_columna():
    # Arrange
    contenido = "Juan,19\nAna,20\nPedro,19"
    esperado = [["Juan", "19"], ["Pedro", "19"]]

    # Act
    resultado = filtrar_por_columna(contenido, 1, "19")

    # Assert
    assert resultado == esperado


# PRUEBA 11: Contar filas
def test_contar_filas():
    # Arrange
    contenido = "nombre,edad\nJuan,19\nAna,20"
    esperado = 3

    # Act
    resultado = contar_filas(contenido)

    # Assert
    assert resultado == esperado


# PRUEBA 12: Contar columnas
def test_contar_columnas():
    # Arrange
    contenido = "nombre,edad,ciudad\nJuan,19,Manizales"
    esperado = 3

    # Act
    resultado = contar_columnas(contenido)

    # Assert
    assert resultado == esperado


# PRUEBA EXTRA: Mocking de una dependencia
def test_leer_csv_usando_mocking():
    # Arrange
    contenido = "nombre,edad\nJuan,19"
    esperado = [["nombre", "edad"], ["Juan", "19"]]

    # Act
    with patch(
        "src.csv_parser.parse_csv_line",
        side_effect=lambda linea: linea.split(",")
    ) as mock_parse:
        resultado = leer_csv_como_lista(contenido)

    # Assert
    assert resultado == esperado
    assert mock_parse.call_count == 2
