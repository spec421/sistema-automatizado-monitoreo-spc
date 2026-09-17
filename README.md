# Sistema Automatizado de Monitoreo

Este repositorio contiene la implementación de un *pipeline* de datos (ETL) para automatizar el Control Estadístico de Procesos (SPC) en un entorno de manufactura. El proyecto procesa mediciones continuas de sensores para generar Cartas de Control $\bar{x}$ y $R$, facilitando la detección de anomalías y apoyando las estrategias de mantenimiento predictivo.

## Objetivo del Proyecto
Sustituir el cálculo manual de límites de control estadístico mediante un script automatizado que limpia, procesa y evalúa miles de registros industriales, conectando los resultados a un tablero interactivo para la toma de decisiones operativas.

## Conjunto de Datos (Dataset)
Se utilizó el **AI4I 2020 Predictive Maintenance Dataset**, el cual simula mediciones de sensores (como velocidad de rotación) en una línea de producción.

## Tecnologías y Herramientas
*   **Lenguaje:** Python 3.x
*   **Manipulación:** NumPy, Pandas
*   **Visualización:** Power BI
*   **Metodología de Calidad:** Core Tools (SPC - Statistical Process Control)

## Metodología
1. **Extracción y Transformación:** Se programó un script en Python para agrupar mediciones continuas en subgrupos constantes ($n=5$).
2. **Cálculo Estadístico:** Se calcularon de forma automatizada las medias ($\bar{x}$) y rangos ($R$) de cada subgrupo, así como los Límites de Control Superior (UCL) e Inferior (LCL) utilizando las constantes estadísticas industriales ($A_2, D_3, D_4$).
3. **Carga y Visualización:** Los datos procesados se exportaron en un formato estructurado (CSV) y se conectaron de forma nativa a Power BI para el desarrollo de un *dashboard* interactivo.

## Resultados Principales
* Procesamiento automatizado de **2,000 subgrupos** de datos en segundos.
* Detección exitosa de **34 alertas de calidad** fuera de los límites de control estadístico.
* Creación de un tablero ejecutivo dinámico que elimina la necesidad de recalcular las fórmulas de SPC manualmente, ahorrando tiempo de análisis y previniendo posibles fallas en la maquinaria.

## Vista del Tablero (Dashboard)
*<img width="863" height="491" alt="image" src="https://github.com/user-attachments/assets/5891f8fb-6852-40d1-a6e1-c94e18b8257b" />
*

## Referencias
S. Matzka, "Explainable Artificial Intelligence for Predictive Maintenance Applications," 2020 Third International Conference on Artificial Intelligence for Industries (AI4I), 2020, pp. 69-74, doi: 10.1109/AI4I49448.2020.00023.

## Cómo ejecutar el proyecto
1. Clona este repositorio:
   ```bash
   git clone https://github.com/spec421/sistema-automatizado-monitoreo-spc.git
