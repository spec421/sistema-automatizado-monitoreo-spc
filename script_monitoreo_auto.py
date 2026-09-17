# -*- coding: utf-8 -*-
import kagglehub
import pandas as pd
import numpy as np
import sqlite3

# Descargamos la base de datos directamente de kaggle.
path = kagglehub.dataset_download("stephanmatzka/predictive-maintenance-dataset-ai4i-2020")

print("Path to dataset files:", path)

print("--- INICIANDO PIPELINE DE DATOS SPC ---")

# 1. EXTRACCIÓN
df = pd.read_csv(path + "/ai4i2020.csv")
#df.head()

# Seleccionamos una variable para monitorear, en este caso será 'Rotational speed [rpm]'
datos_sensor = df['Rotational speed [rpm]'].values

# 2. TRANSFORMACIÓN
# Seleccionamos un número de muestras, en este caso cinco.
n = 5
registros_totales = (len(datos_sensor) // n ) * n
datos_recortados = datos_sensor[:registros_totales]

# Creamos los subgrupos
subgrupos = datos_recortados.reshape(-1, n)

# Calculamos las medias y los rangos
medias_x = np.mean(subgrupos, axis=1)
rangos_r = np.ptp(subgrupos, axis=1)

# Calculamos las medias globales
gran_media = np.mean(medias_x)
rango_medio = np.mean(rangos_r)

# Constantes para n = 5
A2 = 0.577
D3 = 0.0
D4 = 2.114

# Calculamos los Límites de Control
ucl_x = gran_media + (A2 * rango_medio)
lcl_x = gran_media - (A2 * rango_medio)

ucl_r = D4 * rango_medio
lcl_r = D3 * rango_medio

# Creamos un DataFrame limpio con los resultados listos para Power BI
df_spc = pd.DataFrame({
    'Id_Subgrupo': np.arange(1, len(medias_x) + 1),
    'Media_X': medias_x,
    'Rango_R': rangos_r,
    'Gran_Media': gran_media,
    'LCL_X': lcl_x,
    'UCL_X': ucl_x,
    'Rango_Medio': rango_medio,
    'LCL_R': lcl_r,
    'UCL_R': ucl_r
})

# Agregamos banderas para detectar si un punto está fuera de control
df_spc['Alarma_X'] = np.where((df_spc['Media_X'] > ucl_x) | (df_spc['Media_X'] < lcl_x), 1, 0)

print(f"Subgrupos procesados: {len(df_spc)}")
print(f"Alertas de calidad detectadas: {df_spc['Alarma_X'].sum()}")

# 3. CARGA
# Guardamos los resultados en un archivo CSV
nombre_archivo = 'control_calidad_spc.csv'

# Exportamos el DataFrame a CSV.
df_spc.to_csv(nombre_archivo, index=False, encoding='utf-8')

print(f"--- PIPELINE COMPLETADO. ARCHIVO '{nombre_archivo}' CREADO ---")