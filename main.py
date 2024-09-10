import auth
import tasks
import utils
import logging
from datetime import datetime

# Configuración del logging
logging.basicConfig(filename='logs.log', 
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("Inicio del programa MyTask.")
    
    print("""
          ======================================================
          |                                                    |
          |             BIENVENIDO A MyTask                    |
          |                                                    |
          ======================================================
        """)
    
    user_logged = False

    while True:
        
        if not user_logged:

            print("""
              =================== Ingreso ================
              1. Iniciar sesión
              2. Registrarse
              3. Salir del programa
              ======================================================
            """)

            opcion = input("Seleccione una opción: ").strip()
            print("")

            if opcion == '1':
                username = input("Nombre de usuario: ").strip()
                password = input("Contraseña: ").strip()
                user_logged = auth.login(username, password)
                if user_logged:
                    logging.info(f"Usuario {username} ha iniciado sesión.")
                else:
                    logging.warning(f"Intento fallido de inicio de sesión para el usuario {username}.")

            elif opcion == '2':
                username = input("Nombre de usuario: ").strip()
                password = input("Contraseña: ").strip()
                user_logged = auth.register(username, password)
                if user_logged:
                    logging.info(f"Usuario {username} se ha registrado exitosamente.")
                else:
                    logging.warning(f"Registro fallido para el usuario {username}.")

            elif opcion == '3':
                logging.info("Salir del programa.")
                return
            
            else:
                print("Opción no válida")
                logging.warning(f"Opción no válida ingresada: {opcion}.")
                continue

            if not user_logged:
                continue


        print("""
            ===== MENÚ PRINCIPAL =====
            1. Ver todas mis tareas
            2. Crear nueva tarea
            3. Actualizar tarea
            4. Filtrar tareas
            5. Buscar tarea
            6. Eliminar tarea
            7. Eliminar todas las tareas
            8. Cerrar sesión
            9. Salir del programa
            ===========================
            """)

        option = input("Selecciona una opción: ").strip()

        if option == "1":
            tasks.list_tasks(username)
            logging.info(f"Usuario {username} ha visualizado todas las tareas.")
            print("\n===========================")
            input("Enter para volver al Menú: ").strip()
        
        elif option == "2":
            title = input("Título: ").strip()
            description = input("Descripción: ").strip()
            due_date = input("Fecha de vencimiento (DD-MM-YYYY): ").strip()
            label = input("Etiqueta: ").strip()

            try:
                datetime.strptime(due_date, "%d-%m-%Y")
            except ValueError:
                print("Formato de fecha no válida")
                logging.warning(f"Fecha no válida proporcionada por el usuario {username}: {due_date}.")
                continue

            print("")
            print("La nueva tarea a agregar será:\n")
            print(f"  Título: {title}")
            print(f"  Descripción: {description}")
            print(f"  Fecha de vencimiento: {due_date}")
            print(f"  Etiqueta: {label}")
            print(f"  Estado: pendiente")
            print("")

            cancelar = input("Esta correcto?\n1. Confirmar\n2. Cancelar\n").strip()
            print("")
            if cancelar == "1":
                tasks.create_task(username, title, description, due_date, label)
                logging.info(f"Usuario {username} ha creado una nueva tarea: {title}.")
            elif cancelar == "2":
                logging.info(f"Operación de creación de tarea cancelada por el usuario {username}.")
                continue
            else:
                print("Opcion no valida, cancelando operacion")
                logging.warning(f"Opción no válida para confirmar la tarea por el usuario {username}: {cancelar}.")
                continue

        elif option == "3":
            index = int(input("Índice de tarea a actualizar: ").strip()) - 1
            tasks.update_task(index, username)
            logging.info(f"Usuario {username} ha actualizado la tarea con índice {index + 1}.")

        elif option == "4":
            print("Selecciona la opción de filtrado:")
            print("1. Filtrar por etiqueta")
            print("2. Filtrar por estado")
            print("3. Filtrar por fecha de vencimiento")
            
            filter_option = input("Selecciona una opción: ").strip()
            if filter_option == "1":
                label = input("Ingresa la etiqueta: ").strip()
                filtered_tasks = utils.filter_tasks_by_label(tasks.load_tasks(username), label)
                tasks.show_tasks_with_id(filtered_tasks)
                logging.info(f"Usuario {username} ha filtrado tareas por etiqueta: {label}.")
            elif filter_option == "2":
                status = input("Ingresa el estado (pendiente, en progreso o completada): ").strip()
                filtered_tasks = utils.filter_tasks_by_status(tasks.load_tasks(username), status)
                tasks.show_tasks_with_id(filtered_tasks)
                logging.info(f"Usuario {username} ha filtrado tareas por estado: {status}.")
            elif filter_option == "3":
                date = input("Ingresa la fecha de vencimiento (DD-MM-YYYY): ").strip()
                filtered_tasks = utils.filter_tasks_by_expiration_date(tasks.load_tasks(username), date)
                tasks.show_tasks_with_id(filtered_tasks)
                logging.info(f"Usuario {username} ha filtrado tareas por fecha de vencimiento: {date}.")
            else:
                print("Opción no válida, cancelando operación")
                logging.warning(f"Opción de filtrado no válida seleccionada por el usuario {username}: {filter_option}.")
                continue

            print("\n===========================")
            input("Enter para volver al Menú: ").strip()


        elif option == "5":
            print("Selecciona la opción de búsqueda:")
            print("1. Búsqueda por título")
            print("2. Búsqueda por descripción")
            
            search_option = input("Selecciona una opción: ").strip()

            if search_option == "1":
                title = input("Ingresa el título: ").strip()
                task = utils.search_task_by_title(tasks.load_tasks(username), title)
                if task:
                    print("La tarea más cercana al título ingresado es: ")
                    tasks.show_tasks_with_id([task])
                    logging.info(f"Usuario {username} ha buscado tarea por título: {title}.")
                else:
                    print("Tarea no encontrada.")
                    logging.info(f"No se encontró tarea con el título proporcionado por el usuario {username}: {title}.")
            elif search_option == "2":
                description = input("Ingresa la descripción: ").strip()
                task = utils.search_task_by_description(tasks.load_tasks(username), description)
                if task:
                    print("La tarea más cercana a la descripción ingresada es: ")
                    tasks.show_tasks_with_id([task])
                    logging.info(f"Usuario {username} ha buscado tarea por descripción: {description}.")
                else:
                    print("Tarea no encontrada.")
                    logging.info(f"No se encontró tarea con la descripción proporcionada por el usuario {username}: {description}.")
            else:
                print("Opción no válida, cancelando operación")
                logging.warning(f"Opción de búsqueda no válida seleccionada por el usuario {username}: {search_option}.")
                continue

            print("\n===========================")
            input("Enter para volver al Menú: ").strip()

        elif option == "6":
            index = int(input("Índice de tarea a eliminar: ").strip()) - 1
            tasks.delete_task(index, username)
            logging.info(f"Usuario {username} ha eliminado la tarea con índice {index + 1}.")

        elif option == "7":
            tasks.delete_all(username)
            logging.info(f"Usuario {username} ha eliminado todas las tareas.")

        elif option == "8":
            user_logged = False
            logging.info(f"Usuario {username} ha cerrado sesión.")

        elif option == "9":
            logging.info("Salir del programa.")
            return

        else:
            print("Opción no válida.")
            logging.warning(f"Opción no válida ingresada: {option}.")

if __name__ == "__main__":
    main()