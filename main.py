import auth
import tasks



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

            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                username = input("Nombre de usuario:")
                password = input("Contraseña:")
                user_logged = auth.login(username, password)

            elif opcion == '2':
                username = input("Nombre de usuario:")
                password = input("Contraseña:")
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

        option = input("Selecciona una opción: ")

        if option == "1":
            tasks.list_tasks(username)
            print("\n===========================")
            input("Enter para volver al Menú: ")
        
        elif option == "2":
            title = input("Título: ")
            description = input("Descripción: ")
            due_date = input("Fecha de vencimiento (YYYY-MM-DD): ")
            label = input("Etiqueta: ")

            print("La nueva tarea a agregar será:\n")
            print(f"  Título: 'title'")
            print(f"  Descripción: 'description'")
            print(f"  Fecha de vencimiento: 'due_date'")
            print(f"  Etiqueta: 'label'")
            print(f"  Estado: abierto")

            cancelar = input("Esta correcto?\n1. Confirmar\n2. Cancelar\n")
            if cancelar == "1":
                tasks.create_task(username, title, description, due_date, label)
            elif cancelar == "2":
                continue
            else:
                print("Opcion no valida, cancelando operacion")
                continue

        elif option == "3":
            index = int(input("Índice de tarea a actualizar: ")) - 1
            tasks.update_task(index, username)

        # elif option == "4":
        # elif option == "5":
        
        elif option == "6":
            index = int(input("Índice de tarea a eliminar: ")) - 1
            tasks.delete_task(index, username)
        
        elif option == "7":
            tasks.delete_all(index, username)

        elif option == "8":
            user_logged = False

        elif option == "9":
            return

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()