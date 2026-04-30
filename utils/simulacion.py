import random
from datetime import datetime, timedelta

def generar_simulacion(numeroSimulaciones):
    nombres = ["Amelia", "Mariana", "Jose", "Carlos", "Beatriz"]
    materias = ["Programación", "Base de Datos", "Matemáticas", "Inglés"]
    
    simulaciones = []
    for _ in range(numeroSimulaciones):
        simulacion = {
            "id": random.randint(100, 999),
            "nombre": random.choice(nombres),
            "materia_favorita": random.choice(materias),
            "fecha_registro": (datetime(2026, 1, 1) + timedelta(days=random.randint(0, 60))).strftime("%Y/%m/%d")
        }
        
        # Inyectando errores controlados (suciedad)
        if random.random() < 0.1: # 10% de probabilidad de error
            simulacion["materia_favorita"] = None
        if random.random() < 0.05:
            simulacion["nombre"] = simulacion["nombre"] + "_123"
            
        simulaciones.append(simulacion)
        
    return simulaciones