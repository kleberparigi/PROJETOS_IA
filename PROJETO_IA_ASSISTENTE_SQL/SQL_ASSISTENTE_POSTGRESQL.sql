-- Criação da tabela 'vendas'
CREATE TABLE vendas (
    id SERIAL PRIMARY KEY,
    data DATE,
    produto TEXT,
    regiao TEXT,
    valor NUMERIC(10, 2),
    quantidade INTEGER
);

-- Exemplo de inserção (opcional)
-- INSERT INTO vendas (data, produto, regiao, valor, quantidade)
-- VALUES ('2024-05-01', 'Notebook', 'Sudeste', 3200.50, 2);
