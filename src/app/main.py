import streamlit as st

 
st.title("Manipulando eventos Streamlit.")

btn = st.button('Clique aqui')
if btn:
    st.write('Botão clicado!')

st.markdown('---')

check = st.checkbox('Escolha uma das opções:')
if check:
    st.write('checkbox() ativado.')
#   print(check)

st.markdown('---')

radio_choice = st.radio('Escolha uma fruta: ', 
                        [
                            '',
                            'Maça',
                            'Banana',
                            'Melancia',
                            'Acerola',
                            'Melão'
                        ],
                        index=0
)
st.write(f'Opção escolhida: {radio_choice}.')

st.markdown('---')

st.header('--- Selectbox() ---')
select_choice = st.selectbox('Escolha uma fruta: ', 
                        [
                            '',
                            'Maça',
                            'Banana',
                            'Melancia',
                            'Acerola',
                            'Melão'
                        ], index=0
)
st.write(f'Opção escolhida: {select_choice}.')

st.markdown('---')

st.header('--- multiselect() ---')
multiselect_choice = st.multiselect('Escolha uma fruta: ', 
                        [
                            '',
                            'Maça',
                            'Banana',
                            'Melancia',
                            'Acerola',
                            'Melão'
                        ]
)
st.write(f'Opção escolhida: {" ".join(multiselect_choice)}.')

