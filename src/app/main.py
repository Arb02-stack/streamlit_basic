import streamlit as st
from pathlib import Path

# entrada de estilização CSS direto no código
# st.markdown(
#     """
#     <style>
#     .stNumberInput p {
#         width: 100%;
#         padding: 5px 15px;
#         border-radius: 5px;
#         background-color: #48374e;
#     }
#     .stMarkdown p {
#         padding-left: 15px;
#         border-radius: 5px;
#         background-color: #795c82;
#     }
#     </style>    
#     """,
#     unsafe_allow_html=True
# )

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
 
st.title("Entranda de valores Streamlit.")

num = st.number_input('Informe um valor: ', min_value=1, max_value=999, value=10)
st.write(f'Valor informado: {num}')

text = st.text_input('Informe seu nome: ')
st.write(f'Nome: {text}')

st.markdown('---')

st.write('Seleção por Data/Horário')
st_date = st.date_input('Selecione a data: ')
st.write(f'Data selecionada: {st_date}')

st_time = st.time_input('Selecione um horário: ')
st.write(f'Horário selecionado: {st_time}')

descri = st.text_area("Deixe aqui seu opinião:")
st.write(f'Descrição: {descri}')


