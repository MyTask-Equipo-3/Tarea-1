print("""
          ======================================================
          |                                                    |
          |             BIENVENIDO A MyTask                    |
          |                                                    |
          ======================================================
          """)

tareas = [
    {
        "titulo": "Comprar comida",
        "descripcion": "Ir al supermercado y comprar víveres",
        "fecha_vencimiento": "2024-09-30",
        "etiqueta": "personal",
        "estado": "pendiente"
    },
    {
        "titulo": "Terminar informe",
        "descripcion": "Completar el informe de ventas para este trimestre",
        "fecha_vencimiento": "2024-09-25",
        "etiqueta": "trabajo",
        "estado": "en progreso"
    }
]

for idx, tarea in enumerate(tareas, start=1):
        print(f"\nTarea {idx}:")
        print(f"  Título: {tarea['titulo']}")
        print(f"  Descripción: {tarea['descripcion']}")
        print(f"  Fecha de vencimiento: {tarea['fecha_vencimiento']}")
        print(f"  Etiqueta: {tarea['etiqueta']}")
        print(f"  Estado: {tarea['estado']}")

cancelar = input("Esta correcto?\n1. Confirmar\n2. Cancelar")

current = False

if not current:
        print("a")