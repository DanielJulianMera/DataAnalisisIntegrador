# Análisis de Insuficiencia Cardíaca

## Descripción

Este proyecto tiene como objetivo analizar un conjunto de datos relacionado con la insuficiencia cardíaca, con el fin de obtener información relevante sobre los pacientes, como la edad promedio y la cantidad de fumadores por género. El conjunto de datos utilizado es "mstz/heart_failure" de la biblioteca Hugging Face Datasets.

## Requisitos

Para ejecutar el código de este proyecto, necesitarás las siguientes bibliotecas de Python:

- pandas
- numpy
- datasets (de Hugging Face)

## Estructura del Código

El código realiza las siguientes operaciones:

1. Carga el conjunto de datos "mstz/heart_failure".
2. Convierte el conjunto de datos en un DataFrame de pandas.
3. Crea dos DataFrames separados: uno para pacientes vivos (`data_a`) y otro para pacientes fallecidos (`data_b`).
4. Calcula la edad promedio de los pacientes en cada DataFrame.
5. Imprime los tipos de datos de cada columna en el DataFrame original.
6. Calcula y muestra la cantidad de fumadores por género.

## Resultados

Algunos insights obtenidos del análisis son:

- La edad promedio de los pacientes en el estudio.
- La distribución de fumadores por género, lo que puede proporcionar información sobre posibles factores de riesgo relacionados con el género.

## Conclusión

El análisis de los datos de insuficiencia cardíaca proporciona información valiosa sobre las características de los pacientes, incluyendo su edad y hábitos de fumar. Estos insights pueden ser útiles para comprender mejor los factores de riesgo asociados con la insuficiencia cardíaca y para desarrollar estrategias de prevención y tratamiento.
