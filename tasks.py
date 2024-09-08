import json
import utils

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


def show_tasks_with_id(tareas):
    for tarea in tareas:
        print(f"\nTarea {tarea['id']}:")
        print(f"  Título: {tarea['titulo']}")
        print(f"  Descripción: {tarea['descripcion']}")
        print(f"  Fecha de vencimiento: {tarea['fecha_vencimiento']}")
        print(f"  Etiqueta: {tarea['etiqueta']}")
        print(f"  Estado: {tarea['estado']}")

def show_tasks(tareas):
    for idx, tarea in enumerate(tareas, start=1):
        print(f"\nTarea {idx}:")
        print(f"  Título: {tarea['titulo']}")
        print(f"  Descripción: {tarea['descripcion']}")
        print(f"  Fecha de vencimiento: {tarea['fecha_vencimiento']}")
        print(f"  Etiqueta: {tarea['etiqueta']}")
        print(f"  Estado: {tarea['estado']}")

# Función para ver todas las tareas
def list_tasks(username):
    tareas = load_tasks(username)
    if not tareas:
        print("No hay tareas.")
        return
    
    show_tasks(tareas)
    

def update_task(index, username):

    tareas = load_tasks(username)
    if index < 0 or index >= len(tareas):
        print("Número de tarea inválido.")
        return


    title = input("Actualizar título (deja en blanco para mantener): ")
    description = input("Actualizar descripción (deja en blanco para mantener): ")
    due_date = input("Actualizar fecha de vencimiento (YYYY-MM-DD) (deja en blanco para mantener): ")
    label = input("Actualizar etiqueta (deja en blanco para mantener): ")
    status = input("Actualizar etiqueta (deja en blanco para mantener): ")

    if title:
        tareas[index]['titulo'] = title
    if description:
        tareas[index]['descripcion'] = description
    if due_date and utils.validar_fecha(due_date):
        tareas[index]['fecha_vencimiento'] = due_date
    if label:
        tareas[index]['etiqueta'] = label
    if status:
        # Asegúrate de que el estado sea válido antes de actualizar
        if status in ['pendiente', 'en progreso', 'completada']:
            tareas[index]['estado'] = status
        else:
            print("Estado inválido. No se actualizó el estado.")

    save_tasks(username, tareas)
    print("Tarea actualizada con éxito.")

# Función para eliminar una tarea
def delete_task(index, username):

    tareas = load_tasks(username)
    
    if index < 0 or index >= len(tareas):
        print("Número de tarea inválido.")
        return
    
    tarea_eliminada = tareas.pop(index)
    save_tasks(username, tareas)
    print("Tarea '{tarea_eliminada['title']}' eliminada con éxito.")

# Función para eliminar todas las tareas de un usuario
def delete_all(username):
    # Cargar las tareas actuales del archivo
    tasks = load_tasks(username)
    
    # Verificar si ya no hay tareas
    if not tasks:
        print(f"El usuario {username} no tiene tareas para eliminar.")
        return
    
    # Sobrescribir las tareas del usuario con una lista vacía
    save_tasks(username, [])
    print(f"Todas las tareas del usuario {username} han sido eliminadas con éxito.")