def filter_tasks_by_label(tasks,label):
    for i in range(1,len(tasks) + 1):
        tasks[i - 1] = tasks[i - 1] | {"id":i}
    return list(filter(lambda task: task["etiqueta"] == label,tasks))

def filter_tasks_by_expiration_date(tasks,date):
    for i in range(1,len(tasks) + 1):
        tasks[i - 1] = tasks[i - 1] | {"id":i}
    return list(filter(lambda task: task["fecha_vencimiento"] == date,tasks))

def filter_tasks_by_status(tasks,status):
    for i in range(1,len(tasks) + 1):
        tasks[i - 1] = tasks[i - 1] | {"id":i}
    return list(filter(lambda task: task["estado"] == status,tasks))

# Distancia de leveshtein para poder buscar palabras con error.
def levenshtein_distance(s1,s2):
    DP = [[int(1e9) for _ in range(len(s2) + 1)] for __ in range(len(s1) + 1)]
    DP[0][0] = 0
    for i in range(1,len(s1) + 1):
        DP[i][0] = i
    for j in range(1,len(s2) + 1):
        DP[0][j] = j
    for i in range(1,len(s1) + 1):
        for j in range(1,len(s2) + 1):
            DP[i][j] = min(DP[i][j],DP[i - 1][j] + 1)
            DP[i][j] = min(DP[i][j],DP[i][j - 1] + 1)
            DP[i][j] = min(DP[i][j],DP[i - 1][j - 1] + int(s1[i - 1] != s2[j - 1]))
    return DP[len(s1)][len(s2)]

def search_task_by_title(tasks,title):
    distance = int(1e9)
    searched_task = None
    for i,task in enumerate(tasks,start=1):
        d = levenshtein_distance(task["titulo"].lower(),title.lower())
        if d < distance:
            d = distance
            searched_task = task
            searched_task["id"] = i
    return searched_task

def search_task_by_description(tasks,description):
    distance = int(1e9)
    searched_task = None
    for i,task in enumerate(tasks,start=1):
        d = levenshtein_distance(task["titulo"].lower(),description.lower())
        if d < distance:
            d = distance
            searched_task = task
            searched_task["id"] = i
    return searched_task

