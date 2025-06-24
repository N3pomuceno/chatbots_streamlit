import streamlit as st

def gera_ficha_paciente():
    pass




st.title("HeAIthy")
st.subheader("O sistema que ajudará você a ter mais saúde! 😁")

st.caption("Por favor, tenham em mente que esse é um projeto amigável só para ter ideias em cima da utilização de IA, e não é uma boa prática utilizar desse meio como fonte de informação para cuidar da saúde, caso precise de fato, por favor ir a um profissional na área.")

st.markdown(
"""
### Descrição
Esse é um trabalho interessante que quer utilizar de IA, para te ajudar a seguir um estilo de vida mais saudável.
Claro que no fundo isso é uma brincadeira, mas podemos utilizar para fins práticos em alguns meios, quem sabe até como forma de sugerir ideias para o profissional.

A ideia é que seja um meio de perguntas e respostas, tipo um chatbot, que dado as informações preenchidas pelo usuário, a IA pode dar algumas dicas gerais e algumas sugestões para melhorar a vida do usuário em relação a sua saúde.

Sem maiores delongas... 

"""
)

with st.form("health_form"):
    st.markdown("### Formulário")
    Nome = st.text_input(
        label = "Nome Completo",
        key = "Name"
    )
    Idade = st.number_input(
        label = "Idade",
        key = "Age",
        value= 25
    )
    Peso = st.number_input(
        label= "Peso (Kg)",
        key= "Weight",
        value = 70
    )
    genero = st.radio(
        label = "Gênero",
        key= "gender",
        options=["Homem", "Mulher", "Outros"]
    )

    ativFisica = st.radio(
        "Qual é o seu grau de Atividade Física?",
        ["Não faço atividade física", "Pouca atividade física",
        "Faço atividade física constante"],
        captions = ["Nem tenta?", "Duas vezes por semana.", "Três vezes por semana para cima."]
    )

    submitted = st.form_submit_button(
        "Enviar",
        on_click=gera_ficha_paciente
        )



