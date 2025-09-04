import threading

# Creamosuna barrera para sincronizar dos hilos
barrera = threading.Barrier(2)

# Función que ejecutala tarea de imprimir un mensaje y esperar en la barrera
def tarea():
    print("Hilo iniciado")
    # Esperamos en la barrera
    barrera.wait()
    print("Hilo continuando")

# Creamosdos hilos que ejecutarán la misma tarea
hilo1 = threading.Thread(target=tarea)
hilo2 = threading.Thread(target=tarea)

# Iniciamos los hilos
hilo1.start()
hilo2.start()

# Esperamos a que ambos hilos terminen
hilo1.join()
hilo2.join()

print("Programa terminado")