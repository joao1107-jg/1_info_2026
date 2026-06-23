salario = float(input("Digite o salário: "))
cargo = input("Digite o cargo: ")

if cargo == "Programador de Sistemas":
    novo_salario = salario + (salario * 0.30)
    print("Novo salário:", novo_salario)

elif cargo == "Analista de Sistemas":
    novo_salario = salario + (salario * 0.20)
    print("Novo salário:", novo_salario)

elif cargo == "Analista de Banco de Dados":
    novo_salario = salario + (salario * 0.15)
    print("Novo salário:", novo_salario)

else:
    print("Cargo inválido")
