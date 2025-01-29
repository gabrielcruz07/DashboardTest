import pandas as pd
import streamlit as st
from create import create
from delete import delete

st.set_page_config(layout="wide", page_title="Data manager", page_icon=":material/edit:")
st.title("Planilhas Teste")

def build_sidebar():
    st.sidebar.title("Menu Principal")
    page = st.sidebar.selectbox("Selecione a Página", ["Create", "Delete"])
    return page

def build_main(page):
    file_path = "banco.xlsx"
    data = pd.read_excel(file_path, engine="openpyxl")
    
    colunas = st.columns(11)
    dados = {}

    for i, col in enumerate(colunas, start=1):
        with col:
            dados[f"dado{i}"] = st.text_input(label=f"Dado{i}:")

    if st.button("Salvar"):
        new_row = pd.DataFrame([[dados[f"dado{i}"] for i in range(1, 12)]], columns=data.columns)
        data = pd.concat([data, new_row], ignore_index=True)

        with pd.ExcelWriter(file_path, engine="openpyxl", mode="w") as writer:
            data.to_excel(writer, index=False)

        st.success("Planilha atualizada com sucesso!")
        
        st.rerun()

    st.write("Planilha Atualizada:")
    st.dataframe(data)

    if page == "Create":
        create()
    elif page == "Delete":
        delete()
    else:
        st.error("Página não encontrada.")

page = build_sidebar()
build_main(page)
