import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")

st.title("Planilhas Teste")
st.sidebar.title("Teste")

file_path = "Painel_dezembro.xlsm"
data = pd.read_excel(file_path, engine="openpyxl")

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    dado1 = st.text_input(label="Dado1:")
with col2:
    dado2 = st.text_input(label="Dado2:")
with col3:
    dado3 = st.text_input(label="Dado3:")
with col4:
    dado4 = st.text_input(label="Dado4:")
with col5:
    dado5 = st.text_input(label="Dado5:")
with col6:
    dado6 = st.text_input(label="Dado6:")

if st.button("salvar"):
    
    new_row = pd.DataFrame([[dado1, dado2, dado3, dado4, dado5, dado6]], columns=data.columns)

    data = pd.concat([data, new_row], ignore_index=True)

    with pd.ExcelWriter(file_path, engine="openpyxl", mode="w") as writer:
        data.to_excel(writer, index=False)

    st.success("Planilha atualizada com sucesso")

st.write("Planilha Atualizada:")
st.dataframe(data)
