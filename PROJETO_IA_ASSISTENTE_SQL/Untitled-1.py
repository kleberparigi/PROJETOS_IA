# Recriando o conteúdo do README após reset

readme_content = """
# 🤖 Assistente SQL com IA + Dashboards Automáticos

Este projeto é um MVP (mínimo produto viável) criado por **Kleber Parigi Pinto** para unir o poder da **linguagem natural**, **inteligência artificial** (OpenAI) e **visualização de dados** (Plotly + Streamlit) em uma solução prática para analistas de dados, DBAs e profissionais de BI.

---

## 🚀 O que este projeto faz?

1. O usuário digita uma pergunta em linguagem natural (ex: "qual o total de vendas por região em 2023?")
2. O sistema utiliza IA (OpenAI GPT-4) para **converter a pergunta em uma query SQL**
3. A query é executada sobre uma base de dados (SQLite ou PostgreSQL)
4. Os dados são exibidos em tabela e **visualizações automáticas com gráficos**

---

## 🛠️ Tecnologias utilizadas

- `Python`
- `Streamlit`
- `OpenAI GPT-4 API`
- `SQLite / PostgreSQL`
- `Pandas`
- `Plotly Express`

---

## 📦 Estrutura de arquivos

- `app.py`: código principal com interface Streamlit
- `vendas.db`: base de dados SQLite de exemplo
- `dados_vendas.xlsx`: base de dados em Excel (fictícia) para testes reais
- `README.md`: este documento

---

## 💡 Como usar

1. Clone o repositório:
```bash
git clone https://github.com/seuusuario/seurepo.git
cd seurepo
