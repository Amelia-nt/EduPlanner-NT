import random
from datetime import datetime

def generar_usuarios_eduplanner(cantidad):
    print(f"--- INICIANDO SIMULACIÓN EDUPLANNER ---")
    
    # Listas para elegir al azar 
    nombres_estudiantes = ["Amelia", "Mariana", "Jose", "Carlos", "Beatriz"]
    materias = ["Programación", "Base de Datos", "Matemáticas", "Inglés"]
    
    lista_usuarios_simulados = []

    for i in range(cantidad):
        # Creamos el "objeto" usuario parecido al de Java
        usuario = {
            "id": random.randint(100, 999),
            "nombre": random.choice(nombres_estudiantes),
            "materia_favorita": random.choice(materias),
            "fecha_registro": datetime.now().strftime("%Y/%m/%d")
        }
        lista_usuarios_simulados.append(usuario)
        
        print(f"✅ Usuario generado: {usuario['nombre']} | ID: {usuario['id']} | Materia: {usuario['materia_favorita']}")

    print("--- 🚀 SIMULACIÓN FINALIZADA LOCALMENTE ---")
    return lista_usuarios_simulados

if __name__ == "__main__":
    # Aquí se dice cuántos quiero simular
    mis_usuarios = generar_usuarios_eduplanner(5)