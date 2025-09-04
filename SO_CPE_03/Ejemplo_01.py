import threading

# Definimos una variable globalcompartida
contador_global = 0

# Creamosun objeto mutex
mutex = threading.Lock()


# Funciónque incrementa el contador globalde forma segurautilizando un mutex
def incrementar():
    global contador_global
    # Adquirimos el mutex
    mutex.acquire()
    try:
        # Sección crítica: Incrementamos el contador
        contador_global += 1
    finally:
        # Liberamos el mutex
        mutex.release()


# Función que ejecutala tarea de incrementar el contador un número determinado de veces
def tarea():
    for _ in range(100000):
        incrementar()


# Creamosdos hilos que ejecutarán la misma tarea
hilo1 = threading.Thread(target=tarea)
hilo2 = threading.Thread(target=tarea)

# Iniciamos los hilos
hilo1.start()
hilo2.start()

# Esperamos a que ambos hilos terminen
hilo1.join()
hilo2.join()

# Imprimimos el valorfinal del contadorglobal
print("El valor final del contador global es:", contador_global)