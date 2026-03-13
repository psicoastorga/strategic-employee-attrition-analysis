Análisis Estratégico de Rotación de Empleados

Aplicación de Behavioral Data Science para comprender y predecir la rotación laboral

Proyecto de People Analytics orientado a identificar factores organizacionales y trayectorias profesionales que influyen en la decisión de los empleados de abandonar una empresa.

El análisis combina exploración de datos, construcción de indicadores de carrera y modelado predictivo para transformar datos de recursos humanos en información útil para la toma de decisiones estratégicas.

Dataset utilizado:
IBM HR Employee Attrition Dataset

Contexto del problema

La rotación de empleados (attrition) representa uno de los costos ocultos más relevantes en las organizaciones.

Cuando un empleado abandona la empresa se generan múltiples impactos:

costos de reclutamiento

tiempo de entrenamiento

pérdida de conocimiento organizacional

disrupción en los equipos de trabajo

Desde una perspectiva de People Analytics, la rotación puede analizarse como un fenómeno conductual y organizacional influenciado por:

condiciones laborales

trayectorias profesionales

incentivos organizacionales

características individuales

El objetivo es transformar datos de RRHH en indicadores que permitan anticipar riesgos de abandono.

Objetivo del proyecto

Identificar factores organizacionales, laborales y de desarrollo profesional asociados a la rotación de empleados y construir un modelo predictivo de attrition que permita:

comprender los drivers de rotación

estimar probabilidades individuales de abandono

apoyar decisiones estratégicas de retención de talento

El análisis se realizó sobre un dataset de 1470 empleados con variables demográficas, laborales y de trayectoria dentro de la organización.

Enfoque analítico (Behavioral Data Science)

El proyecto sigue una lógica típica de People Analytics basado en datos conductuales:

1 Exploratory Data Analysis (EDA)

Se analizan patrones de rotación en relación con variables como:

overtime

ingresos

distancia al trabajo

satisfacción laboral

trayectoria dentro de la empresa

Esto permite identificar posibles mecanismos organizacionales asociados a la rotación.

2 Construcción de indicadores de carrera

Además de las variables originales, se diseñaron indicadores analíticos para capturar dinámicas profesionales dentro de la organización.

Ejemplos:

Stagnation Index

Indicador que mide el posible estancamiento profesional combinando:

años en el rol actual

tiempo desde la última promoción

Un mayor valor puede indicar limitadas oportunidades de desarrollo.

Promotion Velocity

Mide la velocidad con la que un empleado progresa dentro de la organización.

Promociones más lentas pueden estar asociadas con mayor probabilidad de abandono.

Loyalty Rate

Aproxima la estabilidad de la trayectoria laboral del empleado dentro de la empresa.

Trayectorias más móviles suelen correlacionar con mayor riesgo de rotación.

3 Modelado predictivo

Se entrenó un modelo de regresión logística para estimar la probabilidad de attrition.

El modelo permite:

identificar variables predictivas relevantes

estimar probabilidades individuales de abandono

explorar perfiles de riesgo dentro de la organización

Principales hallazgos

El análisis exploratorio sugiere que la rotación laboral se relaciona con múltiples factores.

Entre los más relevantes:

Trayectoria profesional

mayor Stagnation Index → mayor probabilidad de attrition

menor Promotion Velocity → mayor riesgo de abandono

Condiciones laborales

empleados que realizan overtime presentan mayor rotación

mayores distancias al trabajo se asocian con mayor abandono

Factores económicos

menores niveles de MonthlyIncome se correlacionan con mayor attrition.

Estos resultados sugieren que la rotación no depende únicamente de variables demográficas, sino también de dinámicas organizacionales y oportunidades de desarrollo.

Implicancias estratégicas para RRHH

Los resultados del análisis sugieren que las organizaciones podrían reducir la rotación mediante estrategias como:

monitorear indicadores de estancamiento profesional

mejorar la movilidad interna

diseñar trayectorias de carrera más claras

identificar empleados con alto riesgo de abandono

Esto posiciona a People Analytics como una herramienta estratégica para la gestión del talento.

Tecnologías utilizadas

Python
Pandas
Matplotlib
Scikit-learn
Jupyter Notebook

Estructura del proyecto
data/
   raw/
      IBM-HR-Employee-Attrition.csv

notebooks/
   01_exploratory_analysis.ipynb
   02_feature_engineering.ipynb
   03_modeling.ipynb

src/
   feature_engineering.py
   modeling.py

README.md
Autor

Carlos Astorga
Psicología + Data Science aplicado a People Analytics

LinkedIn
https://es.linkedin.com/in/psicoastorga
