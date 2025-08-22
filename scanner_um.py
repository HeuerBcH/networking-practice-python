import socket

def meu_scanner_um(): # Este scanner é rápido porque testa uma porta específica de uma vez.

    alvo = 'google.com'
    porta = 80

    # Cria o objeto socket
    socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    resultado = socket_obj.connect_ex((alvo, porta))

    if resultado == 0:
        print(f"A porta {porta} esta [ABERTA] em {alvo}")
    else:
        print(f"A porta {porta} esta [FECHADA] ou o host esta inacessivel")

    socket_obj.close() 

meu_scanner_um()