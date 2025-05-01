import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar o conjunto de dados
df = pd.read_csv(r'C:\projects_ds\vehicles_us\vehicles.csv')

# Cabeçalho do app
st.header("Análise de Anúncios de Veículos Usados nos EUA")

# Botão para exibir histograma
if st.button("Mostrar histograma do preço"):
    st.write("Distribuição de preços dos veículos")
    fig = px.histogram(df, x="price", nbins=50, title="Distribuição dos Preços dos Veículos")
    st.plotly_chart(fig)