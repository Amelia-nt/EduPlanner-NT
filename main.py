import pandas as pd
from utils.simulacion import generar_simulacion
from notebook.limpieza import limpiar_datos
from notebook.descripcion import describir_datos # Importamos la descripción

# 1. Generar
datos = generar_simulacion(1000)
df_sucio = pd.DataFrame(datos)

# 2. Limpiar
df_limpio = limpiar_datos(df_sucio)

# 3. Mostrar reporte y Guardar
# (Asegúrate de haber creado la carpeta 'data' dentro de 'notebook')
describir_datos(df_limpio) 
df_limpio.to_csv('notebook/data/eduplanner_limpio.csv', index=False)
print(" Proceso completado con éxito.")
