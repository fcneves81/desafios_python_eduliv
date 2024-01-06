# Importando a biblioteca Pandas
import pandas as pd

# Criando uma lista de dicionários com os dados das compras
compras = [
  {"Código da compra": "2024001",
   "Nome do produto": "Notebook",
   "Categoria do produto":"Informática",
   "Quantidade comprada": 2,
   "Valor unitário": 3500.00,
   "Valor total":7000.00},
  {"Código da compra": "2024002",
   "Nome do produto": "Teclado",
   "Categoria do produto":"Informática",
   "Quantidade comprada": 5,
   "Valor unitário": 120.00,
   "Valor total":600.00},
  {"Código da compra": "2024003",
   "Nome do produto": "Televisão",
   "Categoria do produto":"Eletrônicos",
   "Quantidade comprada": 1,
   "Valor unitário": 2999.00,
   "Valor total":2999.00},
  {"Código da compra": "2024004",
   "Nome do produto": "Asus Zenfone 8",
   "Categoria do produto":"Smartphone",
   "Quantidade comprada": 1,
   "Valor unitário": 2429.10,
   "Valor total":2429.10},
  
]

# Apenas gera um cabeçalho de exibição
print("*" * 120)
print("VENDAS JANEIRO 2024".center(120))
print("*" * 120)
print()

# Criando um dataframe a partir da lista de dicionários
df = pd.DataFrame(compras)

# Imprimindo o dataframe
print(df)
 