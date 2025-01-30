import pandas as pd
import streamlit as st



def edit():
    st.title("Página edit")
    editPage = st.Page("edit.py", title="Edit entry", icon=":material/edit:")
    file_path = "banco_de_dados.xlsx"
    data = pd.read_excel(file_path, engine="openpyxl")
    
    st.write("Edite os dados abaixo:")
    edited_data = st.data_editor(data)
    if st.button("Salvar"):
        edited_data.to_excel("banco_de_dados.xlsx", engine="openpyxl", index=False)
        st.success("Planilha atualizada com sucesso!")
        