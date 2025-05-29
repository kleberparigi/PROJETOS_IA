# Criar o script SQL para PostgreSQL com base na estrutura da planilha

sql_script = """
-- Criação da tabela 'vendas' no PostgreSQL

CREATE TABLE vendas (
    id SERIAL PRIMARY KEY,
    data DATE,
    produto TEXT,
    regiao TEXT,
    valor NUMERIC(10, 2),
    quantidade INTEGER
);

-- Exemplo de inserção (opcional):
-- INSERT INTO vendas (data, produto, regiao, valor, quantidade)
-- VALUES ('2024-05-01', 'Notebook', 'Sudeste', 3200.50, 2);
"""

# Salvar como arquivo .sql
sql_path = "/mnt/data/script_postgresql_vendas.sql"
with open(sql_path, "w", encoding="utf-8") as f:
    f.write(sql_script)

sql_path
