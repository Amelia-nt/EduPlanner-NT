import pandas as pd
import numpy as np

def limpiar_datos(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()

    # 1. Limpieza de textos (Adaptado a EduPlanner)
    data_frame_limpio["nombre"] = data_frame_limpio["nombre"].astype("string").str.strip().str.lower()
    data_frame_limpio["materia_favorita"] = data_frame_limpio["materia_favorita"].astype("string").str.strip().str.lower()

    # 2. Valores esperados
    materias_ok = ["programación", "base de datos", "matemáticas", "inglés"]
    data_frame_limpio["materia_favorita"] = data_frame_limpio["materia_favorita"].where(
        data_frame_limpio["materia_favorita"].isin(materias_ok), pd.NA
    )

    # 3. Limpieza numérica
    data_frame_limpio["id"] = pd.to_numeric(data_frame_limpio["id"], errors='coerce')
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id"] > 0]

    # 4. Limpieza de FECHAS
    data_frame_limpio["fecha_registro"] = pd.to_datetime(data_frame_limpio["fecha_registro"])
    data_frame_limpio["fecha_registro"] = data_frame_limpio["fecha_registro"].fillna(pd.to_datetime("2026-01-01"))

    # 5. Quitar vacíos
    data_frame_limpio = data_frame_limpio.dropna(subset=["id", "nombre", "materia_favorita"])

    return data_frame_limpio