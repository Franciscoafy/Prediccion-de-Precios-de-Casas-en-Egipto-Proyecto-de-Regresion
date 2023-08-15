


Este repositorio contiene un proyecto de análisis de datos y predicción de precios de casas en Egipto utilizando algoritmos de regresión. El objetivo principal es explorar, preprocesar los datos, aplicar técnicas de escalamiento y construir varios modelos de regresión para predecir con precisión los precios de las casas.

Contenido

El repositorio contiene los siguientes archivos y carpetas principales:

data: Esta carpeta contiene el conjunto de datos utilizado para el proyecto. El archivo de datos, egypt_housing_data.csv, contiene información relevante sobre las casas, incluyendo el número de habitaciones, número de baños y el área en metros cuadrados, junto con los precios reales de las casas.

notebooks: En esta carpeta se encuentran los Jupyter Notebooks utilizados durante el proyecto. Cada notebook abarca una etapa específica del proceso, desde la exploración inicial hasta la construcción y evaluación de modelos. tambien se encuentra la carpeta de scripts donde se encuentran todas aquellas funciones que vamos a utilizar para procesar y visualizar los datos 

models: carpeta donde se encuentran guardados cada uno de los modelos entrenados en formato .PKL

requeriments: carpeta donde se encuentran guardadas las librerias necesarias para trabajar con el codigo 

#Objetivos del Proyecto


Exploración de Datos: El primer paso del proyecto es explorar el conjunto de datos para comprender su estructura y distribución. Se realizará un análisis descriptivo y se generarán visualizaciones para destacar las características clave de los datos.

Preprocesamiento: Se llevará a cabo un proceso de preprocesamiento de datos para tratar con valores faltantes, datos atípicos y características categóricas. Esto asegurará que los datos estén en una forma adecuada para el modelado.

Escalamiento de Características: Dado que los algoritmos de regresión pueden ser sensibles a las escalas de las características, se aplicará escalamiento para normalizar las variables y asegurar que tengan un impacto similar en el modelado.

Construcción de Modelos: Se construirán seis modelos de regresión diferentes utilizando algoritmos como Regresión Lineal, Regresión Ridge, random forest , modelos de esemble y Árboles de Regresión. Cada modelo se ajustará a los datos de entrenamiento y se evaluará su rendimiento utilizando métricas como el error cuadrado medio y el R2 score.

Comparación y Selección del Modelo: Los modelos construidos serán comparados en términos de su rendimiento en los datos de prueba. Se seleccionará el modelo con el mejor rendimiento general para hacer predicciones de precios de casas.