usuario_correto = "aluno"
senha_correta = "12345"

tentativas = 0

while tentativas < 3:
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    
    if usuario == usuario_correto and senha == senha_correta:
        print("Acesso liberado")
        break
    else:
        tentativas += 1
        print("Tente novamente")
    
    if tentativas == 3:
        print("Você tentou 3 vezes")
