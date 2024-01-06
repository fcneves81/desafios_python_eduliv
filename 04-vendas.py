#Importando a biblioteca Pandas
import pandas as pd

# Criando um dicionário de listas com os dados das vendas
vendas = {
  "Produto": ["Teclado", "Mouse", "Caixa de som", "Adaptador Bluetooth", "Teclado", "Mouse", "Caixa de Som", "Adaptador Bluetooth"],
  "Quantidade": [10, 13, 3, 5, 6, 2, 1, 2],
  "Preco": [119.90, 64.90, 84.00, 35.00, 119.90, 64.90, 84.00, 35.00]
}

# Criando um dataframe a partir do dicionário
df = pd.DataFrame(vendas)


# Imprimindo o dataframe
print()
print("*=" * 25, end="*\n")
print("vendas janeiro".upper().center(50))
print("*=" * 25, end="*\n")
print(df)

# Adicionando a coluna valor total comprado
df["Valor Total Comprado"] = df["Quantidade"] * df["Preco"]

# Imprimindo o dataframe com a nova coluna
print()
print("*=" * 37, end="*\n")
print("vendas janeiro - valor total comprado".upper().center(74))
print("*=" * 37, end="*\n")
print(df)

# Agrupando o dataframe pela coluna "produto" e somando as quantidades
total_vendas = pd.DataFrame(df.groupby("Produto")["Quantidade"].sum())

# Imprimindo o resultado
print()
print("*=" * 37, end="*\n")
print("quantidade por produto".upper().center(74))
print("*=" * 37, end="*\n")
print(total_vendas)

# Para calcular o ticket médio, primeiro precisamos do faturamento bruto
# Calculando o faturamento bruto
faturamento_bruto = (df["Quantidade"] * df["Preco"]).sum()

# Calculando o volume total de vendas
volume_total = df["Quantidade"].sum()

# Calculando o ticket médio
ticket_medio = faturamento_bruto / volume_total

# Imprimindo o resultado
print()
print("*=" * 25, end="*\n")
print("ticket medio".upper().center(50))
print("*=" * 25, end="*\n")
print(f"\nO valor do ticket médio é de: R$ {ticket_medio:.2f}")

# Calculando a quantidade média comprada por compra
quantidade_media = df["Quantidade"].mean()

# Imprimindo o resultado
print()
print("*=" * 25, end="*\n")
print("media de itens por compra".upper().center(50))
print("*=" * 25, end="*\n")
print(f"\nA quantidade média de itens por compra é de: {int(quantidade_media)} itens.")

# total vendido por produto.
# Agrupamos o dataframe pela coluna "produto" e somando os preços
total_vendido = pd.DataFrame(df.groupby("Produto")["Valor Total Comprado"].sum())
vendas_geral = df["Valor Total Comprado"].sum()

# Imprimindo o resultado
print()
print("*=" * 25, end="*\n")
print("total comprado por produto".upper().center(50))
print("*=" * 25, end="*\n")
print(total_vendido)
print()
print("*=" * 25, end="*\n")
print("total geral de vendas".upper().center(50))
print("*=" * 25, end="*\n")
print(f"\nO total geral de vendas é de R$ {vendas_geral:.2f}\n")

#Um agradecimento e saudação final
print("*=" * 25, end="*\n")
print("obrigado. bebam água!".upper().center(50))
print("*=" * 25, end="*\n")
print()