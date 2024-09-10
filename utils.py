import logging
from datetime import datetime


def filter_tasks_by_label(tasks, label):
    for i in range(1, len(tasks) + 1):
        tasks[i - 1] = tasks[i - 1] | {"id": i}
    filtered_tasks = list(filter(lambda task: task["etiqueta"] == label, tasks))
    logging.info(f"Filtrado de tareas por etiqueta '{label}'. Se encontraron {len(filtered_tasks)} tareas.")
    return filtered_tasks

def filter_tasks_by_expiration_date(tasks, date):
    for i in range(1, len(tasks) + 1):
        tasks[i - 1] = tasks[i - 1] | {"id": i}
    filtered_tasks = list(filter(lambda task: task["fecha_vencimiento"] == date, tasks))
    logging.info(f"Filtrado de tareas por fecha de vencimiento '{date}'. Se encontraron {len(filtered_tasks)} tareas.")
    return filtered_tasks

def filter_tasks_by_status(tasks, status):
    for i in range(1, len(tasks) + 1):
        tasks[i - 1] = tasks[i - 1] | {"id": i}
    filtered_tasks = list(filter(lambda task: task["estado"] == status, tasks))
    logging.info(f"Filtrado de tareas por estado '{status}'. Se encontraron {len(filtered_tasks)} tareas.")
    return filtered_tasks

def levenshtein_distance(s1, s2):
    DP = [[int(1e9) for _ in range(len(s2) + 1)] for __ in range(len(s1) + 1)]
    DP[0][0] = 0
    for i in range(1, len(s1) + 1):
        DP[i][0] = i
    for j in range(1, len(s2) + 1):
        DP[0][j] = j
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            DP[i][j] = min(DP[i][j], DP[i - 1][j] + 1)
            DP[i][j] = min(DP[i][j], DP[i][j - 1] + 1)
            DP[i][j] = min(DP[i][j], DP[i - 1][j - 1] + int(s1[i - 1] != s2[j - 1]))
    logging.debug(f"Distancia de Levenshtein calculada entre '{s1}' y '{s2}': {DP[len(s1)][len(s2)]}")
    return DP[len(s1)][len(s2)]

def search_task_by_title(tasks, title):
    distance = int(1e9)
    searched_task = None
    for i, task in enumerate(tasks, start=1):
        d = levenshtein_distance(task["titulo"].lower(), title.lower())
        if d < distance:
            distance = d
            searched_task = task
            searched_task["id"] = i
    if searched_task:
        logging.info(f"Tarea encontrada por título '{title}': {searched_task}")
    else:
        logging.info(f"No se encontró tarea con título '{title}'.")
    return searched_task

def search_task_by_description(tasks, description):
    distance = int(1e9)
    searched_task = None
    for i, task in enumerate(tasks, start=1):
        d = levenshtein_distance(task["titulo"].lower(), description.lower())
        if d < distance:
            distance = d
            searched_task = task
            searched_task["id"] = i
    if searched_task:
        logging.info(f"Tarea encontrada por descripción '{description}': {searched_task}")
    else:
        logging.info(f"No se encontró tarea con descripción '{description}'.")
    return searched_task

def verify_date(date_str):
    try:
        task_date = datetime.strptime(date_str, "%d-%m-%Y")
        current_date = datetime.now()

        if current_date.date() <= task_date.date():
            logging.info(f"Fecha '{date_str}' es válida y no ha pasado.")
            return True
        else:
            logging.info(f"Fecha '{date_str}' es pasada.")
            return False
    except ValueError:
        logging.error(f"Error en verificar fecha: '{date_str}'")
        print("Error en verificar fecha.")
        return False
