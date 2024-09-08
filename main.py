import auth
import tasks



def main():
    
    print("Bienvenido al sistema de gestión de tareas.")

    # Autenticación de usuario
    while True:
        print("\n1. Iniciar sesión")
        print("2. Registrarse")
        opcion = input("Seleccione una opción: ")

        username = input("Nombre de usuario:")
        password = input("Contraseña:")

        if opcion == '1':
            break
        elif opcion == '2':
            if auth.register(username, password):
                break
            else:
                print("Error al registrar usuario")
        else:
            print("Opción no válida")

    if auth.login(username, password):
        while True:
            print("\n1. Crear nueva tarea")
            print("2. Ver mis tareas")
            print("3. Cerrar sesión")

            option = input("Selecciona una opción: ")
            
            if option == "1":
                title = input("Título: ")
                description = input("Descripción: ")
                due_date = input("Fecha de vencimiento (YYYY-MM-DD): ")
                label = input("Etiqueta: ")
                tasks.create_task(username, title, description, due_date, label)
            elif option == "2":
                tasks.list_tasks(username)

                print("\n1. Actualizar tarea")
                print("2. Eliminar tarea")
                print("3. Eliminar todas")
                print("4. Volver al menú")

                option = input("Selecciona una opción: ")

                if option == "1":
                    index = int(input("Índice de tarea a actualizar: ")) - 1
                    tareas = tasks.load_tasks(username)
                    if index < 0 or index >= len(tareas):
                        print("Número de tarea inválido.")
                    else:
                        tasks.update_task(index, username)

                elif option == "2":
                    index = int(input("Índice de tarea a eliminar: ")) - 1
                    tasks.delete_task(index)

                elif option == "3":
                    index = int(input("Índice de tarea a eliminar: ")) - 1
                    tasks.delete_task(index, username)

                elif option == "4":
                    index = int(input("Índice de tarea a eliminar: ")) - 1
                    tasks.delete_task(index)

                else:
                    print("Opción no válida.")

            elif option == "3":
                print("Saliendo del sistema.")
                break
            else:
                print("Opción no válida.")
                
    else:
        print("Error al iniciar sesión")

if __name__ == "__main__":
    main()