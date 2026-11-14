import random

participantes = []

print("=== SISTEMA DE RIFA DA FORMATURA ===")
print("Digite o nome do comprador (ou digite 'sair' para encerrar e sortear):\n")

while True:
    nome = input("Nome do participante: ")

    if nome.lower() == "sair":
        break

    if nome == "":
        print("Nome invalido! Por favor, digite um nome valido.")
        continue

    participantes.append(nome)
    print(f"-> {nome} cadastrado com sucesso! (Total: {len(participantes)})")

if len(participantes) > 0:
    ganhador = random.choice(participantes)
    print(f"Total de bilhetes vendidos: {len(participantes)}")
    print(f"O GANHADOR DA RIFA E: {ganhador.upper()}!")
else:
    print("Nenhum participante foi cadastrado. Sorteio cancelado.")
