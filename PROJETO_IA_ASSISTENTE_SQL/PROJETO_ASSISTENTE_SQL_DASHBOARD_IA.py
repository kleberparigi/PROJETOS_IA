# MVP: Assistente de SQL + Gerador de Dashboard com IA

"""
Objetivo:
1. Usuário digita uma pergunta em linguagem natural (ex: "total de vendas por região em 2023")
2. IA converte essa pergunta para uma query SQL com base no schema fornecido
3. Executa a query e gera visualizações automáticas (gráfico de barras, linha, etc.)
4. Interface simples com Streamlit
"""

import streamlit as st
import pandas as pd
import openai
import sqlite3
import plotly.express as px

# CONFIGURAÇÕES INICIAIS
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Conectar a banco de exemplo (você pode trocar por um PostgreSQL, MySQL, etc.)
conn = sqlite3.connect("vendas.db")
cursor = conn.cursor()

def executar_query(query):
    try:
        df = pd.read_sql_query(query, conn)
        return df
    except Exception as e:
        st.error(f"Erro na execução da query: {e}")
        return None

def gerar_query_com_ia(pergunta, schema):
    prompt = f"""
Você é um assistente SQL. Com base no seguinte schema de tabela:
{schema}
Gere uma query SQL para responder à pergunta: "{pergunta}"
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content']

# LAYOUT STREAMLIT
st.title("🤖 Assistente de SQL com IA + Dashboards")

pergunta = st.text_input("Digite sua pergunta em linguagem natural:")

if pergunta:
    # Obter schema do banco (pode ser fixo ou dinâmico)
    schema_exemplo = """
Tabela: vendas
- id (int)
- data (date)
- produto (text)
- regiao (text)
- valor (float)
- quantidade (int)
"""
    query_gerada = gerar_query_com_ia(pergunta, schema_exemplo)
    st.code(query_gerada, language="sql")

    df_resultado = executar_query(query_gerada)
    if df_resultado is not None and not df_resultado.empty:
        st.write("### Resultado da Consulta:")
        st.dataframe(df_resultado)

        # Tentativa de visualização automática
        colunas_numericas = df_resultado.select_dtypes(include=['int64', 'float64']).columns
        colunas_texto = df_resultado.select_dtypes(include=['object']).columns

        if len(colunas_numericas) >= 1 and len(colunas_texto) >= 1:
            fig = px.bar(df_resultado, x=colunas_texto[0], y=colunas_numericas[0])
            st.plotly_chart(fig)
        else:
            st.info("Não foi possível gerar gráfico automaticamente.")
    else:
        st.warning("Nenhum dado retornado.")
