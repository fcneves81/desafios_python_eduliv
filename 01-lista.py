# Criando uma lista vazia para armazenar os produtos
compras = list()

# Imprimindo um cabeçalho com o nome da loja
print()
print("=" * 48)
print("LOJAS LION".center(48))
print("=" * 48) 

#Imprimindo as instruções para o usuário
print("\nDigite o nome do produto e a quantidade desejada.\nPara sair, tecle 'ENTER' sem digitar nada.\n")

#Usando um laço while para repetir o processo de adicionar produtos à lista
while True:
    # Pedindo ao usuário o nome do produto
    adicionar = input("Por favor informe o produto a ser adicionado: ")
    # Verificando se o usuário digitou a condição de parada
    if adicionar == "":
        # Saindo do laço
        break
    else:
        # Atribuindo o nome do produto à variável produto
        produto = adicionar
        # Pedindo ao usuário a quantidade do produto
        quantidade = input("Informe a quantidade para compra: ")
        # Criando um dicionário com o produto como chave e a quantidade como valor
        produtos = {produto : quantidade}
        # Adicionando o dicionário à lista de compras
        compras.append(produtos)
#Verificando se a lista de compras está vazia
if len(compras) == 0:
    print("Você não inseriu nenhum produto na lista!")
else:
    print()
    print("=" * 48)
    print("SEU PEDIDO".center(48))
    print("=" * 48, "\n")    
    # Usando um laço for com enumerate para exibir o índice e o dicionário de cada produto
    for indice, dicionario in enumerate(compras):
        # Imprimindo o índice do item sem quebrar a linha
        print(f"Item {indice + 1}:", end=" ")
        # Usando outro laço for com items para exibir o nome e a quantidade de cada produto
        for prod, qtde in dicionario.items():
            # Imprimindo o nome e a quantidade do produto com formatação
            print(f"{prod:.<35} {qtde:>3}")
# Imprimindo um agradecimento ao usuário
print()      
print("=" * 48)
print("OBRIGADO".center(48))
print("=" * 48, "\n") 