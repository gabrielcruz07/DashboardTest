import pandas as pd
import streamlit as st
from create import create
from edit import edit 
from datetime import datetime

st.set_page_config(layout="wide", page_title="Dashboard Python", page_icon=":material/edit:")
st.title("Planilhas Teste")

query_params = st.query_params

if "page" not in query_params:
    query_params["page"] = "Create"

def build_sidebar():
    st.sidebar.title("Menu Principal")

    page = st.sidebar.selectbox("Selecione a Página", ["Create", "Edit"], index=0 if query_params["page"] == "Create" else 1)

    query_params["page"] = page
    return page

def build_main(page):
    file_path = "banco_de_dados.xlsx"

    if page == "Edit":
        edit()
        return

    data = pd.read_excel(file_path, engine="openpyxl")

    colunas = st.columns(3)
    dados = {}

    for i, col_name in enumerate(data.columns):
        if i == 3:
            dados[col_name] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            continue 

        if i == 7:
            dados[col_name] = "em dia" 
            continue

        if i == 8:
            dados[col_name] = "em aberto"
            continue

        with colunas[i % 3]:
            dados[col_name] = st.text_input(label=col_name)

    if st.button("Salvar"):
        new_row = pd.DataFrame([[dados[col] for col in data.columns if col not in ["coluna4", "coluna8"]]], columns=data.columns)
        data = pd.concat([data, new_row], ignore_index=True)

        with pd.ExcelWriter(file_path, engine="openpyxl", mode="w") as writer:
            data.to_excel(writer, index=False)

        st.success("Planilha atualizada com sucesso!")
        st.rerun()

    st.write("Planilha Atualizada:")
    st.dataframe(data)

    if st.button("Editar"):
        query_params["page"] = "Edit"
        st.rerun()

page = build_sidebar()
build_main(page)

