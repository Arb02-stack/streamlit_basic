import streamlit as st


st.title("Esse é o título 1 [title()].")
st.header("Esse é o título 2 [header()].")
st.subheader("Esse é o título 3 [subheader()].")
st.write("Essa é a função [write()].")
st.caption("Legenda explicativa [caption()].")
st.markdown("---")
st.markdown("""
    # Markdown
    ### Podemos utilizar todos os recursos de markdown() normalmente.
    [streamlit site:](https://docs.streamlit.io/)
""")
st.code("""
    # exibindo um código formatado [code()]
    def soma(x,y):
        return x+y

    print(soma(5,10))
""")
