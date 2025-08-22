import socket

import threading 
from queue import Queue

fila_portas = Queue()
portas_abertas = []

def meu_scanner_tres(): 

    while not fila_portas.empty():
        porta = fila_portas.get()
        try:
            socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_obj.settimeout(1)  # Define um tempo limite de 1 segundo
            if socket_obj.connect_ex((alvo, porta)) == 0:
                portas_abertas.append(porta)
            socket_obj.close()
        except socket.error as e:
            pass

        fila_portas.task_done()

alvo = "127.0.0.1"
for porta in range(1, 1025):
    fila_portas.put(porta)

# Cria e inicia as threads
for _ in range(100):
    thread = threading.Thread(target=meu_scanner_tres)
    thread.daemon = True # Permite que o programa principal saia mesmo se as threads estiverem rodando
    thread.start()

fila_portas.join() # Aguarda até que todas as portas na fila sejam processadas

print(f"Scan concluído no alvo {alvo}.")
if portas_abertas:
    print("Portas abertas encontradas:")
    # Ordena a lista para uma exibição mais limpa
    for porta in sorted(portas_abertas):
        print(f"  - Porta {porta}")
else:
    print("Nenhuma porta aberta encontrada no intervalo escaneado.")
