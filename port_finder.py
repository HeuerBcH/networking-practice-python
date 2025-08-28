import subprocess

# Usando WSL (Windows Subsystem for Linux) para realizar comandos de Terminal Linux e acessar as portas

result = subprocess.run(["wsl", "netstat", "-tuln"], stdout=subprocess.PIPE, text=True)

print("PORTAS STATUS == LISTEN:")
for line in result.stdout.splitlines():
    for word in line.split():
        if word == "LISTEN":
            print(f"PROTOCOL: {line.split()[0].upper()}, PORT: {line.split()[3]}")

# Há maneiras de realizar a busca com Prompt de Comandos Windows, no entanto o exercício foi praticado com WSL
# devido à minha intenção de explorar o ambiente Linux.