import streamlit as st
from pathlib import Path

# Função que carrega o arquivo .css:
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Diretório atual main.py
current_dir = Path(__file__).parent

# Sobe um nível para 'src' e depois entra em 'static/css/style.css'
css_path = current_dir.parent / "static" / "css" / "style.css"

# Aplica o CSS no inicio do script
local_css(css_path)
# ---
 
# SIDEBAR
st.sidebar.title('Streamlit: Sidebar')
st.sidebar.write('Menu de configurações')
name  = st.sidebar.text_input('Informe seu nome:')
check = st.sidebar.checkbox('Ativar notificação')
op    = st.sidebar.selectbox('Escolha uma categoria:', 
    [
        '',
        'Técnologia',
        'Saúde',
        'Educação',
        'Entretenimento'
    ], index=0
)

# body
st.header(f"Bem vind(o)a, {name if name else 'Usuário'}.")
st.markdown('---')
st.write(f'Categoria escolhida: {op}')
st.write(f"Notificação: {'Ativado' if check else 'Desativado'}")

st.markdown('---')

with st.container():
    st.subheader('Perfil do Usuário')
    col1, col2 = st.columns(2)

    with col1:
        st.text_input('Nome')
    with col2:
        st.text_input('Sobrenome')

    st.text_area('Biografia', f"Fale mais sobre você...")

