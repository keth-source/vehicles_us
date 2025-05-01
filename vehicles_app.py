import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar o conjunto de dados
df = pd.read_csv('vehicles.csv')

# Cabeçalho do app
st.header("Análise de Anúncios de Veículos Usados nos EUA")

# Botão para exibir histograma
if st.button("Mostrar histograma do preço"):
    st.write("Distribuição de preços dos veículos")
    fig = px.histogram(df, x="price", nbins=50, title="Distribuição dos Preços dos Veículos")
    st.plotly_chart(fig)

# Caixa de seleção para gráfico de dispersão
if st.checkbox('Mostrar gráfico de dispersão (odômetro vs. preço)'):
    st.write("Gráfico de dispersão entre odômetro e preço")
    fig_scatter = px.scatter(df, x='odometer', y='price', title='Odômetro vs. Preço')
    st.plotly_chart(fig_scatter)