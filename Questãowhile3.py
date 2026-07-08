opcao = -1

while opcao != 0:
    print("\n===== MENU =====")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")
    
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 0:
        print("Programa encerrado.")
    elif opcao in (1, 2, 3, 4):
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        if opcao == 1:
            resultado = num1 + num2
            print(f"Resultado: {resultado}")
        elif opcao == 2:
            resultado = num1 - num2
            print(f"Resultado: {resultado}")
        elif opcao == 3:
            resultado = num1 * num2
            print(f"Resultado: {resultado}")
        elif opcao == 4:
            if num2 != 0:
                resultado = num1 / num2
                print(f"Resultado: {resultado}")
            else:
                print("Erro: divisão por zero!")
    else:
        print("Opção inválida! Tente novamente.")
