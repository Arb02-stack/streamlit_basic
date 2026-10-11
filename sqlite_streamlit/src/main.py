import streamlit as st
from db.methods import insertData


st.title("Cadastro de Clientes")

# Cria o formulário para agrupar e sincronizar os inputs
with st.form("form_cadastro", clear_on_submit=True):
    name = st.text_input("Digite seu nome:", required=True, placeholder="nome")
    email = st.text_input("Digite seu e-mail:", required=True, placeholder="email")
    tel = st.text_input("Digite seu telefone:", required=True, placeholder="telefone")

    # O botão de submissão do formulário
    send = st.form_submit_button("Cadastrar")

# A validação acontece instantaneamente no momento do clique
if send:
    if not name.strip() or not email.strip() or not tel.strip():
        # Se algum estiver vazio, exibe o aviso e bloqueia o envio
        st.error("Preencha todos os campos antes de enviar.")
    else:
        insertData(name, email, tel)
        st.success("Cadastro efetuado com sucesso!")

