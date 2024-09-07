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
            print("\n1. Crear tarea")
            print("2. Buscar tareas")
            print("3. Actualizar tarea")
            print("4. Eliminar tarea")
            print("5. Salir")

            option = input("Selecciona una opción: ")
            
            if option == "1":
                title = input("Título: ")
                description = input("Descripción: ")
                due_date = input("Fecha de vencimiento (YYYY-MM-DD): ")
                label = input("Etiqueta: ")
                tasks.create_task(username, title, description, due_date, label)

            elif option == "2":
                list_tasks()

            elif option == "3":
                index = int(input("Índice de tarea a actualizar: ")) - 1
                title = input("Nuevo título (o deja en blanco para mantener): ")
                description = input("Nueva descripción (o deja en blanco para mantener): ")
                due_date = input("Nueva fecha de vencimiento (YYYY-MM-DD): ")
                label = input("Nueva etiqueta (o deja en blanco para mantener): ")
                update_task(index, {"title": title, "description": description, "due_date": due_date, "label": label})

            elif option == "4":
                index = int(input("Índice de tarea a eliminar: ")) - 1
                delete_task(index)

            elif option == "5":
                print("Saliendo del sistema.")
                break

            else:
                print("Opción no válida.")
                
    else:
        print("Error al iniciar sesión")

if __name__ == "__main__":
    main()