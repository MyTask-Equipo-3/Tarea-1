import json
import hashlib
import logging

# Ruta del archivo JSON que almacena los usuarios
USUARIOS_FILE = 'data/usuarios.json'

def hash_password(password):
    # Devuelve el hash del password
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    try:
        with open(USUARIOS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error("El archivo de usuarios no existe")
        print("El archivo de usuarios no existe")
        return []
    except KeyError:
        logging.error("Error: La clave 'users' no se encuentra en el archivo JSON.")
        print("Error: La clave 'users' no se encuentra en el archivo JSON.")
        return []
    except json.JSONDecodeError:
        logging.error("Error: Formato JSON inválido o archivo vacío.")
        print("Error: Formato JSON inválido o archivo vacío.")
        return []
    except Exception as e:
        logging.error(f"Ocurrió un error inesperado: {e}")
        print(f"Ocurrió un error inesperado: {e}")
        return []

def register(username, password):
    users = load_users()

    if username in [user['username'] for user in users]:
        logging.info(f"El nombre de usuario '{username}' ya existe.")
        print("El nombre de usuario ya existe.\n")
        return False
    else:
        hashed_password = hash_password(password)
        users.append({"username": username, "password": hashed_password})
        
        with open(USUARIOS_FILE, "w") as file:
            json.dump(users, file, indent=4)

        logging.info(f"Usuario {username} registrado con éxito.")
        print(f"Usuario {username} registrado con éxito.\n")
        return True

def login(username, password):
    users = load_users()

    hashed_password = hash_password(password)

    for user in users:
        if user["username"] == username and user["password"] == hashed_password:
            logging.info(f"Inicio de sesión exitoso para el usuario {username}.")
            print("Inicio de sesión exitoso.\n")
            return True
        
    logging.warning(f"Nombre de usuario o contraseña incorrectos para el usuario {username}.")
    print("Nombre de usuario o contraseña incorrectos.\n")
    return False
