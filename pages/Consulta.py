import streamlit as st
import pandas as pd

dados = pd.read_csv("cliente.csv")

st.title("Clientes Cadastrados")
st.divider()

st.dataframe(dados)