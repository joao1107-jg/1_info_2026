while True:
    print("\n" * 50)
    print("#" * 50)
    print("   SISTEMA DE CADASTRO DE USUÁRIOS (TEXTO)")
    print("#" * 50)
    print()
    print("=== LOGIN ===")

    while True:
        usuario = input("Login: ")
        senha = input("Senha: ")

        if usuario == "admin" and senha == "123":
            print(f"Login realizado com sucesso! Bem-vindo, {usuario}")
            input("ENTER para continuar...")
            break
        else:
            print("Usuário ou senha incorretos. Tente novamente.\n")

    print("\n" * 50)
    encerrar = "n"

    while True:
        print("=== MENU PRINCIPAL ===")
        print("Usuário logado: admin")
        print("1 - Inserir usuário")
        print("2 - Pesquisar usuário")
        print("3 - Remover usuário")
        print("4 - Listar todos os usuários")
        print("5 - Logout")
        print("6 - Encerrar")

        opcao = input("Escolha uma opção: ")

        if opcao == "5":
            print("\nSaindo da conta...\n")
            break
        elif opcao == "6":
            print("\nEncerrando o programa...")
            encerrar = "s"
            break
        elif opcao in ("1", "2", "3", "4"):
            print("\n[Ainda não implementado]\n")
        else:
            print("\nOpção inválida! Tente novamente.\n")

    print("\n" * 50)

    if encerrar == "s":
        break
