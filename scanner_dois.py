import socket

def meu_scanner_dois(alvo, porta): # Este scanner é lento porque testa uma porta de cada vez. Se o intervalo for de 1 a 1000, ele fará 1000 tentativas sequenciais.

    try:
        socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_obj.settimeout(1)  # Define um tempo limite de 1 segundo

        if socket_obj.connect_ex((alvo, porta)) == 0:
            print(f"A porta {porta} esta [ABERTA]") 
        else:
            print(f"A porta {porta} esta [FECHADA] ou o host esta inacessivel")
        socket_obj.close()
    except socket.error as e:
        pass

alvo = 'google.com'
porta_inicial = 1
porta_final = 100

print("-" * 50)
print("Escaneando o alvo: ", alvo)
print(f"Intervalo de portas: {porta_inicial} a {porta_final}")
print("-" * 50)

for porta in range(porta_inicial, porta_final + 1):
    meu_scanner_dois(alvo, porta)