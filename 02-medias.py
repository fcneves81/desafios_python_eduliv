# Criando uma lista vazia para armazenar as notas
notas = list()
# Criando uma variável para armazenar a soma das notas
soma = 0

# Imprimindo um cabeçalho com o título do programa
print()
print("=" * 55)
print("MÉDIA DAS NOTAS".center(55))
print("=" * 55) 

# Pedindo ao usuário que informe quantas notas deseja inserir
quantidade = int(input("\nPor favor, informe quantas notas deseja inserir: "))

#Usando um laço for para repetir o processo de pedir e armazenar as notas
for i in range(1,quantidade + 1):
    # Pedindo ao usuário que informe a nota
    nota = float(input(f"Por favor, informe a {i}ª nota: "))
    # Somando a nota à variável soma
    soma += nota
    # Adicionando a nota à lista de notas
    notas.append(nota)
# Calculando a média das notas    
media = soma / quantidade
#Imprimindo a média das notas
print(f"\nA média das notas é: {media}")
# um agradecimento ao usuário antes de finalizar o programa
print()
print("=" * 55)
print("OBRIGADO!".center(55))
print("=" * 55) 