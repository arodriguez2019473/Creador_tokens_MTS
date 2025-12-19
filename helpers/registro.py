import time

SELLADOS = {}


TTL = 3600  # Tiempo de vida en segundos

def registrar(sello):
    SELLADOS[sello] = time.time()

def verificar(sello):

    if sello not in SELLADOS:

        return False

    if time.time() - SELLADOS[sello] > TTL:
        del SELLADOS[sello]
        return False
    
    return True