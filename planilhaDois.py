import pandas as pd
import streamlit as st
from create import create
from delete import delete
import os

# Configuração da página
st.set_page_config(layout="wide", page_title="Data manager", page_icon=":material/edit:")
st.title("Planilhas Teste")

# Função para a barra lateral
def build_sidebar():
    st.sidebar.title("Menu Principal")
    page = st.sidebar.selectbox("Selecione a Página", ["Create", "Delete", "DetalhePedido"])
    return page

# Função principal
def build_main(page):
    file_path = "banco.xlsx"
    
    # Verifica se o arquivo Excel já existe. Se não, cria um novo com as colunas
    if not os.path.exists(file_path):
        df = pd.DataFrame(columns=["Código", "Fabricante", "Qnt", "Qnt Total", 
                                   "Comprador Resp", "Status", "N. Pedido Compras", 
                                   "Previsão Entrega", "fk_pedido"])
        df.to_excel(file_path, index=False, engine="openpyxl")

    # Lê os dados do arquivo Excel
    data = pd.read_excel(file_path, engine="openpyxl")

    # Se a página for "DetalhePedido"
    if page == "DetalhePedido":
        # Aqui você pode pegar os dados que devem ser exibidos para o "DetalhePedido"
        pedido_id = st.text_input("Digite o ID do Pedido")
        
        if pedido_id:
            # Aqui você pode buscar os dados do pedido no arquivo ou em outra fonte
            # Suponhamos que você já tenha os dados em uma tabela ou arquivo, por exemplo:
            pedido_dados = data[data['fk_pedido'] == pedido_id]  # Pegando o pedido com esse fk_pedido
            if not pedido_dados.empty:
                st.write(f"Detalhes do Pedido {pedido_id}:")
                st.dataframe(pedido_dados)
            else:
                st.write("Pedido não encontrado!")
        
    # Se for a página "Create" ou "Delete", segue o fluxo normal
    else:
        # Criando campos de entrada apenas para os campos necessários
        col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns(9)

        # Campos de entrada personalizados
        with col1:
            codigo = st.text_input("Código")

        with col2:
            fabricante = st.text_input("Fabricante")

        with col3:
            qnt = st.text_input("Qnt")

        with col4:
            qntTotal = st.text_input("Qnt Total")

        with col5:
            compradorResp = st.text_input("Comprador Resp")

        with col6:
            status = st.text_input("Status")

        with col7:
            numPedido = st.text_input("N. Pedido Compras")

        with col8:
            prevEntrega = st.text_input("Previsão Entrega")

        with col9:
            fkPedido = st.text_input("fk_pedido")

        # Se o botão "Salvar" for pressionado
        if st.button("Salvar"):
            # Criando uma nova linha com os valores digitados
            new_row = pd.DataFrame([[codigo, fabricante, qnt, qntTotal, compradorResp, 
                                      status, numPedido, prevEntrega, fkPedido]], 
                                   columns=["Código", "Fabricante", "Qnt", "Qnt Total", 
                                            "Comprador Resp", "Status", "N. Pedido Compras", 
                                            "Previsão Entrega", "fk_pedido"])

            # Adiciona a nova linha ao DataFrame existente
            data = pd.concat([data, new_row], ignore_index=True)

            # Salvando no Excel
            with pd.ExcelWriter(file_path, engine="openpyxl", mode="w") as writer:
                data.to_excel(writer, index=False)

            # Mensagem de sucesso
            st.success("Dados adicionados com sucesso!")

            # Recarrega a página para atualizar a tabela
            st.rerun()

        # Exibindo a tabela com os dados
        st.write("### Tabela de Registros")
        st.dataframe(data)

# Chamando as funções corretamente
page = build_sidebar()  # Criando a barra lateral
build_main(page)
