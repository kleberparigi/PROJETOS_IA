# Gerar dados fictícios para simular uma base de vendas e exportar como Excel

import pandas as pd
from faker import Faker
import random

fake = Faker("pt_BR")

# Criar dados simulados
num_linhas = 200
dados = {
    "id": list(range(1, num_linhas + 1)),
    "data": [fake.date_between(start_date="-1y", end_date="today") for _ in range(num_linhas)],
    "produto": [random.choice(["Notebook", "Mouse", "Teclado", "Monitor", "Webcam"]) for _ in range(num_linhas)],
    "regiao": [random.choice(["Sul", "Sudeste", "Centro-Oeste", "Norte", "Nordeste"]) for _ in range(num_linhas)],
    "valor": [round(random.uniform(100, 5000), 2) for _ in range(num_linhas)],
    "quantidade": [random.randint(1, 20) for _ in range(num_linhas)],
}

df = pd.DataFrame(dados)

# Exportar para Excel
excel_path = "/mnt/data/dados_vendas.xlsx"
df.to_excel(excel_path, index=False)

excel_path
