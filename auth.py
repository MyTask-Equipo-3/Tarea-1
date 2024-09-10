import json
import hashlib

# Ruta del archivo JSON que almacena los usuarios
USUARIOS_FILE = 'data/usuarios.json'

def hash_password(password):
    #Devuelve el hash del password
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    try:
        with open(USUARIOS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("El archivo de usuarios no existe")
        return []
    except KeyError:
        print("Error: La clave 'users' no se encuentra en el archivo JSON.")
        return []
    except json.JSONDecodeError:
        print("Error: Formato JSON inválido o archivo vacío.")
        return []
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return []
    
def register(username, password):

    users = load_users()

    if username in [user['username'] for user in users]:
        print("El nombre de usuario ya existe.\n")
        return False
    else:
        hashed_password = hash_password(password)
        users.append({"username": username, "password": hashed_password})
        
        with open(USUARIOS_FILE, "w") as file:
            json.dump(users, file, indent=4)

        print(f"Usuario {username} registrado con éxito.\n")
        return True

def login(username, password):

    users = load_users()

    hashed_password = hash_password(password)

    for user in users:
        if user["username"] == username and user["password"] == hashed_password:
            print("Inicio de sesión exitoso.\n")
            return True
        
    print("Nombre de usuario o contraseña incorrectos.\n")
    return False

