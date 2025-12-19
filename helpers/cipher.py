import time, secrets, hashlib, os

from dotenv import load_dotenv

# que hace el load_dotenv? carga las variables de entorno desde un archivo .env

load_dotenv()

pepe = int(os.getenv('P'))
SERVER_SECRET = int(os.getenv('SERVER_SECRET'))

def generar_papa(user_id:int):

    tiempo = int(time.time())
    non = secrets.randbits(64)

    juan = (user_id + non + tiempo) % pepe

    corazon = pow(juan, SERVER_SECRET, pepe)

    return hashlib.sha256(str(corazon).encode()).hexdigest()

