import random

jogar_novamente = "s"

while jogar_novamente == "s":
    print("Escolha o nível de dificuldade:")
    print("1 - Fácil (1 a 10)")
    print("2 - Médio (1 a 20)")
    print("3 - Difícil (1 a 30)")

    opcao = input("Digite sua opção: ")

    if opcao == "1":
        minimo = 1
        maximo = 10
    elif opcao == "2":
        minimo = 1
        maximo = 20
    else:
        minimo = 1
        maximo = 30

    numero_sorteado = random.randint(minimo, maximo)
    chances = 3

    print(f"\nAdivinhe o número entre {minimo} e {maximo}. Você tem {chances} chances!")

    while chances > 0:
        tentativa = int(input("Digite seu palpite: "))
        chances -= 1

        if tentativa == numero_sorteado:
            print("Parabéns, você acertou!")
            break
        elif tentativa < numero_sorteado:
            print("Você errou! Tente um número maior")
        else:
            print("Você errou! Tente um número menor")

        if chances == 0:
            print(f"Você perdeu! Fim de jogo. O número era {numero_sorteado}.")

    jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").lower()

print("Obrigado por jogar!")
