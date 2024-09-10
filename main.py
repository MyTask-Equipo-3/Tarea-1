import auth
import tasks
import utils
from datetime import datetime

def main():
    
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

            elif opcion == '2':
                username = input("Nombre de usuario: ").strip()
                password = input("Contraseña: ").strip()
                user_logged = auth.register(username, password)

            elif opcion == '3':
                return
            
            else:
                print("Opción no válida")
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
            elif cancelar == "2":
                continue
            else:
                print("Opcion no valida, cancelando operacion")
                continue

        elif option == "3":
            index = int(input("Índice de tarea a actualizar: ").strip()) - 1
            tasks.update_task(index, username)

        elif option == "4":
            print("Selecciona la opción de filtrado:")
            print("1. Filtrar por etiqueta")
            print("2. Filtrar por estado")
            print("3. Filtrar por fecha de vencimiento")
            
            filter_option = input("Selecciona una opción: ").strip()
            if filter_option == "1":
                label = input("Ingresa la etiqueta: ").strip()
                tasks.show_tasks_with_id(
                    utils.filter_tasks_by_label(
                        tasks.load_tasks(username),
                        label
                    )
                )
            elif filter_option == "2":
                status = input("Ingresa el estado (pendiente, en progreso o completada): ").strip()
                tasks.show_tasks_with_id(
                    utils.filter_tasks_by_status(
                        tasks.load_tasks(username),
                        status
                    )
                )
            elif filter_option == "3":
                date = input("Ingresa la fecha de vencimiento (DD-MM-YYYY): ").strip()
                tasks.show_tasks_with_id(
                    utils.filter_tasks_by_expiration_date(
                        tasks.load_tasks(username),
                        date
                    )
                )
            else:
                print("Opción no válida, cancelando operación")
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
                else:
                    print("Tarea no encontrada.")
            elif search_option == "2":
                description = input("Ingresa la descripción: ").strip()
                task = utils.search_task_by_description(tasks.load_tasks(username), description)
                if task:
                    print("La tarea más cercana a la descripción ingresada es: ")
                    tasks.show_tasks_with_id([task])
                else:
                    print("Tarea no encontrada.")
            else:
                print("Opción no válida, cancelando operación")
                continue

            print("\n===========================")
            input("Enter para volver al Menú: ").strip()

        elif option == "6":
            index = int(input("Índice de tarea a eliminar: ").strip()) - 1
            tasks.delete_task(index, username)
        
        elif option == "7":
            tasks.delete_all(username)

        elif option == "8":
            user_logged = False

        elif option == "9":
            return

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()