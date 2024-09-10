import json
import utils
import logging
from datetime import datetime

# Función para obtener la ruta del archivo de tareas del usuario
def get_tasks_file(username):
    return f"data/tareas_{username}.json"

# Función para cargar las tareas de un usuario
def load_tasks(username):
    tasks_file = get_tasks_file(username)
    try:
        with open(tasks_file, 'r') as file:
            tasks = json.load(file)
        logging.info(f"Tareas cargadas para el usuario {username}.")
        return tasks
    except FileNotFoundError:
        logging.error(f"No se encontró el archivo de tareas para el usuario {username}.")
        return []

# Función para guardar las tareas de un usuario
def save_tasks(username, tareas):
    tasks_file = get_tasks_file(username)
    try:
        with open(tasks_file, 'w') as file:
            json.dump(tareas, file, indent=4)
        logging.info(f"Tareas guardadas para el usuario {username}.")
        return True
    except FileNotFoundError:
        logging.error(f"No se encontró el archivo de tareas para el usuario {username}.")
        return False

def create_task(username, title, description, due_date, label):
    new_task = {
        "titulo": title,
        "descripcion": description,
        "fecha_vencimiento": due_date,
        "etiqueta": label,
        "estado": "pendiente"
    }

    if utils.verify_date(due_date):
        tareas = load_tasks(username)
        tareas.append(new_task)
        save_tasks(username, tareas)
        print("Tarea creada exitosamente.")
        logging.info(f"Tarea creada exitosamente para el usuario {username}: {new_task}.")
    else:
        print("Tarea no creada. Se ingresó una fecha pasada.")
        logging.warning(f"Tarea no creada para el usuario {username}. Fecha pasada: {due_date}.")

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
        logging.info(f"No hay tareas para el usuario {username}.")
        return
    
    show_tasks(tareas)
    logging.info(f"Tareas listadas para el usuario {username}.")
    

def update_task(index, username):
    tareas = load_tasks(username)
    if index < 0 or index >= len(tareas):
        print("Número de tarea inválido.")
        logging.error(f"Índice de tarea inválido para el usuario {username}: {index}.")
        return

    title = input("Actualizar título (deja en blanco para mantener): ").strip()
    description = input("Actualizar descripción (deja en blanco para mantener): ").strip()
    due_date = input("Actualizar fecha de vencimiento (DD-MM-YYYY) (deja en blanco para mantener): ").strip()

    try:
        datetime.strptime(due_date, "%d-%m-%Y")
    except ValueError:
        print("Formato de fecha no válida.")
        logging.error(f"Formato de fecha no válida proporcionado por el usuario {username}: {due_date}.")
        return
    
    label = input("Actualizar etiqueta (deja en blanco para mantener): ").strip()
    status = input("Actualizar estado (pendiente, en progreso o completada) (deja en blanco para mantener): ").strip()

    if title:
        tareas[index]['titulo'] = title
    if description:
        tareas[index]['descripcion'] = description
    if due_date:
        if utils.verify_date(due_date):
            tareas[index]['fecha_vencimiento'] = due_date
        else:
            print("Tarea no actualizada. Se ingresó una fecha pasada.")
            logging.warning(f"Tarea no actualizada para el usuario {username}. Fecha pasada: {due_date}.")
            return
    if label:
        tareas[index]['etiqueta'] = label
    if status:
        if status in ['pendiente', 'en progreso', 'atrasada', 'completada']:
            tareas[index]['estado'] = status
        else:
            print("Estado no válido. No se actualizó el estado.")
            logging.warning(f"Estado no válido proporcionado por el usuario {username}: {status}.")
            return

    save_tasks(username, tareas)
    print("Tarea actualizada con éxito.")
    logging.info(f"Tarea actualizada con éxito para el usuario {username}: {tareas[index]}.")

# Función para eliminar una tarea
def delete_task(index, username):
    tareas = load_tasks(username)
    
    if index < 0 or index >= len(tareas):
        print("Número de tarea inválido.")
        logging.error(f"Índice de tarea inválido para el usuario {username}: {index}.")
        return
    
    tarea_eliminada = tareas.pop(index)
    save_tasks(username, tareas)
    print(f"Tarea {tarea_eliminada['titulo']} eliminada con éxito.")
    logging.info(f"Tarea eliminada con éxito para el usuario {username}: {tarea_eliminada['titulo']}.")

# Función para eliminar todas las tareas de un usuario
def delete_all(username):
    # Cargar las tareas actuales del archivo
    tasks = load_tasks(username)
    
    # Verificar si ya no hay tareas
    if not tasks:
        print("No se encontro ninguna tarea.")
        logging.info(f"No hay tareas para eliminar para el usuario {username}.")
        return
    
    # Sobrescribir las tareas del usuario con una lista vacía
    save_tasks(username, [])
    print(f"Todas las tareas del usuario {username} han sido eliminadas con éxito.")
    logging.info(f"Todas las tareas del usuario {username} han sido eliminadas con éxito.")