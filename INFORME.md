# INFORME — ANÁLISIS Y MEJORA DE PRUEBAS UNITARIAS

**Universidad Nacional de Colombia — Sede Manizales**  
**Asignatura:** Introducción a DevOps  
**Docente:** César Augusto Palacios Alarcón  
**Estudiante:** Juan Sebastián Rivera  
**Grupo:** Pendiente de completar  
**Fecha:** 14 de octubre de 2026  
**Repositorio:** https://github.com/Juanserive10/pruebas_unitarias_devops

---

## 1. Introducción

El presente informe documenta el análisis, diseño, ejecución y mejora de pruebas unitarias sobre el repositorio `pruebas_unitarias_devops`.

El trabajo se desarrolló utilizando Python 3.13.5, pytest 8.0.0, pytest-cov 4.0.0, Git, GitHub y AWS CloudShell como entorno Linux de ejecución.

Se trabajó sobre un fork del repositorio original del docente. Las pruebas, correcciones y ampliaciones de cobertura se registraron mediante commits descriptivos, con el propósito de mantener trazabilidad sobre la evolución del código.

Se seleccionaron tres módulos: `calculadora.py`, `descuentos.py` y `csv_parser.py`.

Los resultados finales fueron 59 pruebas exitosas, seis errores corregidos y una cobertura combinada del 95 % en los tres módulos seleccionados.

## 2. Objetivos

### Objetivo general

Evaluar y mejorar la calidad de funciones Python mediante pruebas unitarias estructuradas, identificación de errores y medición de cobertura.

### Objetivos específicos

- Diseñar pruebas utilizando la estructura AAA.
- Identificar comportamientos incorrectos mediante casos normales y casos límite.
- Corregir al menos tres bugs encontrados.
- Alcanzar una cobertura mínima del 85 % en los módulos trabajados.
- Registrar el proceso mediante commits en Git.
- Utilizar mocking para aislar dependencias.
- Documentar los hallazgos y resultados obtenidos.

## 3. Metodología

Se utilizó pytest como framework de pruebas y pytest-cov para medir cobertura.

Las pruebas se organizaron siguiendo el patrón AAA:

**Arrange:** preparación de los valores de entrada y resultados esperados.

**Act:** ejecución de la función que se desea evaluar.

**Assert:** comparación entre el resultado obtenido y el comportamiento esperado.

Para los errores que debían producir excepciones se utilizó `pytest.raises(ValueError)`.

El proceso de corrección siguió una secuencia de detección, reproducción, solución y verificación.

Inicialmente se diseñaron pruebas que fallaban frente al código original. Posteriormente, se modificaron las funciones correspondientes y se ejecutaron nuevamente las pruebas. Los avances se registraron en commits independientes para facilitar la revisión del historial.

## 4. Análisis por módulo

### 4.1. Módulo calculadora.py

**Responsabilidad:** implementar operaciones matemáticas básicas y funciones de procesamiento numérico.

Se analizaron las funciones de suma, resta, multiplicación, división, potencia, raíz cuadrada, promedio, máximo, mínimo, área y perímetro de rectángulos.

Se diseñaron 15 pruebas para verificar operaciones normales, números negativos, listas vacías y situaciones que requieren excepciones.

**Justificación de las pruebas:**

Se buscó comprobar tanto los resultados habituales como los comportamientos que podrían provocar errores. Por ejemplo, dividir entre cero debe generar una excepción controlada, mientras que calcular el mínimo de una lista debe devolver un elemento real de dicha lista.

**Hallazgos:**

1. La función `raiz_cuadrada()` no rechazaba números negativos.
2. La función `minimo()` inicializaba incorrectamente su variable auxiliar en cero.

Ambos problemas fueron corregidos.

**Resultado:** 15 pruebas exitosas y 93 % de cobertura.

### 4.2. Módulo descuentos.py

**Responsabilidad:** calcular descuentos comerciales, impuestos, precios finales y descuentos por volumen.

Se probaron descuentos simples, acumulativos, apilados y por cantidad de unidades.

Se diseñaron 23 pruebas para evaluar porcentajes válidos e inválidos, precios negativos, impuestos negativos, listas vacías y umbrales de cantidad.

**Justificación de las pruebas:**

Las operaciones de descuentos afectan directamente los importes económicos de una compra. Por esta razón, se verificaron tanto los resultados monetarios como las validaciones que impiden valores fuera de rango.

**Hallazgos:**

1. `calcular_precio_final()` aplicaba el impuesto al precio original en lugar del precio descontado.
2. `descuento_apilado()` no devolvía un resultado para listas no vacías y carecía del manejo requerido para descuentos superiores al 100 %.

Se corrigió el cálculo del impuesto y se completó la función de descuentos apilados, limitando el porcentaje total al 100 %.

**Resultado:** 23 pruebas exitosas y 95 % de cobertura.

### 4.3. Módulo csv_parser.py

**Responsabilidad:** procesar información CSV, convertir registros, validar estructuras, filtrar y extraer columnas.

Se diseñaron 21 pruebas para evaluar campos normales, campos con comas entre comillas, comillas escapadas, filas incompletas, contenido vacío y operaciones de extracción y filtrado.

**Justificación de las pruebas:**

Los archivos CSV pueden contener comas como parte de los valores, columnas ausentes y estructuras irregulares. Por tanto, las pruebas debían verificar que el procesamiento no dependiera únicamente de separar cadenas mediante comas.

**Hallazgos:**

1. `parse_csv_line()` no interpretaba adecuadamente las comillas ni las comas contenidas en campos delimitados.
2. `csv_a_diccionarios()` omitía las claves correspondientes a columnas faltantes.

Se utilizó `csv.reader` junto con `StringIO` para interpretar los campos y se ajustó la conversión a diccionarios para completar los valores faltantes con cadenas vacías.

**Resultado:** 21 pruebas exitosas y 96 % de cobertura.

## 5. Registro de bugs encontrados

| N.º | Módulo y función | Entrada que revela el bug | Resultado erróneo | Resultado esperado | Corrección aplicada |
|---|---|---|---|---|---|
| 1 | `calculadora.raiz_cuadrada()` | `-4` | Devuelve un resultado complejo en lugar de lanzar una excepción | `ValueError` | Validar si el número es negativo antes de calcular |
| 2 | `calculadora.minimo()` | `[5, 8, 3]` | Devuelve `0` | Devuelve `3` | Inicializar `min_val` con `lista[0]` |
| 3 | `descuentos.calcular_precio_final()` | Precio 100000, impuesto 19 %, descuento 10 % | `109000` | `107100` | Calcular el impuesto sobre el precio descontado |
| 4 | `descuentos.descuento_apilado()` | Precio 100000, descuentos `[50, 60]` | Devuelve `None` | Devuelve `0`, según la regla adoptada | Completar la función y limitar el descuento acumulado al 100 % |
| 5 | `csv_parser.parse_csv_line()` | `Juan,"Manizales, Caldas",19` | Separa incorrectamente el campo entre comillas | Tres campos correctamente interpretados | Sustituir `split()` por `csv.reader` |
| 6 | `csv_parser.csv_a_diccionarios()` | Cabecera `nombre,edad,ciudad` y fila `Juan,19` | Omite la clave `ciudad` | Incluye `"ciudad": ""` | Recorrer todas las cabeceras y completar las columnas faltantes |

### Análisis de los bugs

Los errores encontrados fueron de naturaleza diversa.

Los errores de calculadora estaban relacionados con entradas no contempladas e inicialización incorrecta de variables.

Los errores de descuentos afectaban reglas de cálculo monetario y tratamiento de porcentajes.

Los errores de CSV se relacionaban con la interpretación de formatos estructurados y el manejo de registros incompletos.

Las pruebas permitieron reproducir los comportamientos incorrectos antes de modificar el código y comprobar posteriormente que las correcciones solucionaban los casos identificados.

## 6. Prueba con mocking

Se implementó una prueba que utiliza `unittest.mock.patch` para sustituir temporalmente la función `parse_csv_line()` durante una llamada a `leer_csv_como_lista()`.

La prueba proporciona una implementación simulada y verifica tanto el resultado producido como el número de invocaciones de la dependencia.

Esto permite comprobar la interacción entre funciones sin depender de la implementación real de `parse_csv_line()`.

El módulo analizado recibe contenido CSV como cadenas de texto. Por esta razón, la prueba no requiere crear ni leer archivos físicos.

Debe aclararse que el mock sustituye una dependencia interna y no una operación de lectura mediante `open()`.

## 7. Resultados de cobertura

### 7.1. Herramientas

- Python 3.13.5
- pytest 8.0.0
- pytest-cov 4.0.0
- AWS CloudShell
- Git y GitHub

### 7.2. Comando utilizado

```bash
python -m pytest tests/ -v \
  --cov=src.calculadora \
  --cov=src.descuentos \
  --cov=src.csv_parser \
  --cov-report=term-missing
```

### 7.3. Salida del reporte

```text
Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
src/calculadora.py      44      3    93%   55,68,74
src/csv_parser.py       76      3    96%   57,68,126
src/descuentos.py       62      3    95%   80,98,105
--------------------------------------------------
TOTAL                  182      9    95%

59 passed in 0.16s
```

### 7.4. Interpretación

Se ejecutaron exitosamente las 59 pruebas unitarias implementadas.

Los tres módulos superaron individualmente la meta mínima del 85 %.

De las 182 instrucciones ejecutables consideradas por el instrumento de cobertura, nueve quedaron sin ejecutar, obteniéndose una cobertura combinada del 95 %.

La medición general del directorio `src/` también incluye módulos no seleccionados, por lo que su porcentaje resulta inferior. Para verificar el cumplimiento de la consigna se utilizó la cobertura específica de los tres módulos trabajados.

La cobertura obtenida demuestra un alcance amplio de las pruebas, pero no garantiza que todas las entradas posibles o todos los comportamientos estén correctamente evaluados.

## 8. Trazabilidad mediante Git y GitHub

El repositorio se obtuvo mediante un fork del proyecto original del docente y se clonó en AWS CloudShell.

Los cambios se registraron progresivamente:

1. Incorporación de pruebas iniciales de calculadora.
2. Corrección de raíz cuadrada con negativos.
3. Corrección de la función mínimo.
4. Ampliación de pruebas y detección del error de impuestos.
5. Corrección del cálculo de impuestos.
6. Pruebas para descuentos apilados.
7. Corrección de descuentos apilados.
8. Ampliación de cobertura de descuentos.
9. Incorporación de pruebas CSV y mocking.
10. Corrección del procesamiento de comillas CSV.
11. Corrección de columnas faltantes.
12. Ampliación de cobertura CSV.

Esta separación facilita identificar qué problema motivó cada modificación, observar el estado previo y posterior a las correcciones y comprender la evolución del proyecto.

## 9. Reflexión final

### ¿Qué no mide la cobertura?

La cobertura de código indica qué líneas o instrucciones fueron ejecutadas durante las pruebas, pero no demuestra por sí sola que el comportamiento del programa sea correcto.

Una prueba podría ejecutar una línea sin verificar adecuadamente su resultado. También pueden existir combinaciones de datos, condiciones lógicas y situaciones no contempladas, incluso cuando el porcentaje de cobertura es elevado.

Por esa razón, considero que la cobertura debe interpretarse junto con la calidad de las afirmaciones, la selección de casos límite y la capacidad de las pruebas para descubrir errores reales.

### ¿Qué aprendí?

Este taller permitió comprender que las pruebas unitarias no consisten únicamente en verificar operaciones que normalmente funcionan. También es necesario diseñar entradas que expongan las debilidades de una implementación.

La estructura AAA ayudó a separar la preparación de datos, la ejecución y la comprobación de resultados, haciendo que los casos fueran más fáciles de entender y mantener.

La experiencia de detectar primero los errores y corregirlos después permitió evidenciar la utilidad de una metodología de pruebas reproducibles.

También fue importante el uso de Git. Registrar las pruebas y correcciones mediante commits separados hizo posible conservar un historial de la evolución del código, aspecto esencial para la trazabilidad y la colaboración en proyectos de software.

Finalmente, el uso de pytest, mocking y mediciones de cobertura mostró que la calidad del software requiere tanto herramientas automáticas como análisis crítico del comportamiento esperado.

## 10. Conclusiones

Se desarrollaron 59 pruebas unitarias con estructura AAA sobre tres módulos Python.

Se identificaron y corrigieron seis bugs, manteniendo evidencia de los fallos y registrando las modificaciones en el historial de GitHub.

Se alcanzó una cobertura del 93 % en calculadora, 95 % en descuentos y 96 % en CSV, cumpliendo el objetivo establecido.

El ejercicio permitió integrar pruebas unitarias, depuración de código, aislamiento de dependencias, control de versiones y documentación técnica dentro de un mismo flujo de trabajo.

---

**Repositorio de entrega:**  
https://github.com/Juanserive10/pruebas_unitarias_devops
