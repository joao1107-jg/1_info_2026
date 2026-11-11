produtos = []

while True:
    nome_produto = input("Digite o nome do produto eletrônico: ")
    produtos.append(nome_produto)
    
    continuar = input("Deseja adicionar outro produto? (s/n): ").lower()
    
    if continuar != 's':
        break
        
print("\n--- Lista de Produtos Eletrônicos ---")
for i, produto in enumerate(produtos, 1):
    print(f"{i}. {produto}")
