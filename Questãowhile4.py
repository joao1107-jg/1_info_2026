soma = 0
quantidade = 0
maior = 0

while True:
    numero = int(input("Digite um número: "))

    if numero < 0:
        break

    soma += numero
    quantidade += 1

    if quantidade == 1 or numero > maior:
        maior = numero

if quantidade > 0:
    media = soma / quantidade
    print(f"Soma: {soma}")
    print(f"Média: {media:.2f}")
    print(f"Maior número: {maior}")
else:
    print("Nenhum número positivo foi informado.")
