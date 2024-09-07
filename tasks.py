import json

# Función para obtener la ruta del archivo de tareas del usuario
def get_tasks_file(username):
    return f"data/tareas_{username}.json"

# Función para cargar las tareas de un usuario
def load_tasks(username):

    tasks_file = get_tasks_file(username)

    try:
        with open(tasks_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Función para guardar las tareas de un usuario
def save_tasks(username, tareas):
    tasks_file = get_tasks_file(username)
    try:
        with open(tasks_file, 'w') as file:
            json.dump(tareas, file, indent=4)
        return True
    except FileNotFoundError:
        return False


def create_task(username, title, description, due_date, label):

    new_task = {
        "titulo": title,
        "descripcion": description,
        "fecha_vencimiento": due_date,
        "etiqueta": label,
        "estado": "pendiente"
    }

    #validar fecha?

    tareas = load_tasks(username)
    tareas.append(new_task)
    if not save_tasks(username, tareas):
        print("Tarea no creada.")
    print("Tarea creada exitosamente.")


# Función para ver todas las tareas
def ver_tareas(usuario):
    tareas = load_tasks(usuario)
    if not tareas:
        print("No hay tareas.")
        return
    
    for idx, tarea in enumerate(tareas, start=1):
        print(f"\nTarea {idx}:")
        print(f"  Título: {tarea['titulo']}")
        print(f"  Descripción: {tarea['descripcion']}")
        print(f"  Fecha de vencimiento: {tarea['fecha_vencimiento']}")
        print(f"  Etiqueta: {tarea['etiqueta']}")
        print(f"  Estado: {tarea['estado']}")