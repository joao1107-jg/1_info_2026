palavra_secreta = "PYTHON"
letras_certas = []
erros_maximos = 6
erros_atuais = 0

print("#########################################")
print("  JOGO DE ADIVINHAÇÃO DE PALAVRAS (FORCA)")
print("#########################################\n")

while erros_atuais < erros_maximos:
    print("\nPalavra: ", end="")
    letras_faltando = 0
    
    for letra in palavra_secreta:
        if letra in letras_certas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
            letras_faltando += 1
            
    print()
    
    if letras_faltando == 0:
        print("\nParabéns! Você venceu e descobriu a palavra!")
        break
        
    print(f"Erros: {erros_atuais} de {erros_maximos}")
    tentativa = input("Digite uma letra: ").upper()
    
    if tentativa in palavra_secreta:
        print(f"Muito bem! A letra '{tentativa}' existe na palavra.")
        if tentativa not in letras_certas:
            letras_certas.append(tentativa)
    else:
        print(f"Que pena! A letra '{tentativa}' NÃO existe na palavra.")
        erros_atuais += 1

if erros_atuais == erros_maximos:
    print("\nGame Over! Você atingiu o limite de erros.")
    print(f"A palavra secreta era: {palavra_secreta}")
