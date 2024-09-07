import json
import hashlib
#import getpass

# Ruta del archivo JSON que almacena los usuarios
USUARIOS_FILE = 'data/usuarios.json'

def hash_password(password):
    """Devuelve el hash del password"""
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    try:
        with open(USUARIOS_FILE, "r") as file:
            return json.load(file)   #["users"]?
    except FileNotFoundError:
        return []
    
def register(username, password):

    users = load_users()

    if username in [user['username'] for user in users]:
        print("El nombre de usuario ya existe.")
    else:
        hashed_password = hash_password(password)
        users.append({"username": username, "password": hashed_password})
        
        try:
            with open(USUARIOS_FILE, "w") as file:
                json.dump({"users": users}, file, indent=4)
        except FileNotFoundError:
            return False

        print(f"Usuario {username} registrado con éxito.")
        return True

def login(username, password):

    users = load_users()

    hashed_password = hash_password(password)

    for user in users:
        if user["username"] == username and user["password"] == hashed_password:
            print("Inicio de sesión exitoso.")
            return True
        
    print("Nombre de usuario o contraseña incorrectos.")
    return False

