import pandas as pd
import numpy as np
import random
from datetime import datetime

def crear_simulacion_sucia(cantidad=1000):
    nombres_estudiantes = ["Amelia", "Mariana", "Jose", "Carlos", "Beatriz"]
    materias = ["Programación", "Base de Datos", "Matemáticas", "Inglés"]
    
    lista_usuarios = []
    for _ in range(cantidad):
        usuario = {
            "id": random.randint(100, 999),
            "nombre": random.choice(nombres_estudiantes),
            "materia_favorita": random.choice(materias),
            "fecha_registro": datetime.now().strftime("%Y/%m/%d")
        }
        lista_usuarios.append(usuario)
    
    df = pd.DataFrame(lista_usuarios)

    # --- ENSUCIAR DATOS (Inyectar errores) ---
    # 1. Meter nulos (NaN)
    for _ in range(30):
        df.loc[random.randint(0, cantidad-1), 'materia_favorita'] = np.nan
    
    # 2. Meter nombres con números o errores
    df.loc[0, 'nombre'] = "Amelia123"
    df.loc[1, 'materia_favorita'] = "progra_error"

    # Guardar en la carpeta data
    df.to_csv('data/eduplanner_sucio.csv', index=False)
    print("✅ Archivo 'eduplanner_sucio.csv' creado en carpeta data.")

if __name__ == "__main__":
    crear_simulacion_sucia()