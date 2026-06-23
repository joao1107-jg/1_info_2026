idade = int(input("Digite sua idade: "))
habilitacao = input("Possui habilitação? (sim ou não): ")

if idade >= 18 and habilitacao == "sim":
    print("Pode dirigir")

else:
    print("Não pode dirigir")
