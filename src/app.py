import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from config.connect import initialize


initialize()
openai = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0)

template = '''
Você é um analista financeiro.
Escreva um relatório financeiro detalhado para a empresa "{empresa}" para o período {period}.

O relatório deve ser escrito em {language} e incluir a seguinte análise:
{analysis}

Certifique-se de fornecer insights e conclusões para esta seção.
'''
#Formate o relatório utilizando Markdown

prompt_template = PromptTemplate.from_template(template=template)

companies = ['ACME Corp', 'Globex Corporation', 'Soylent Corp', 'Initech', 'Umbrella Corporation']
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
years = [2021, 2022, 2023, 2024]
languages = ['Português', 'Inglês', 'Espanhol', 'Francês', 'Alemão']
analysis = [
    "Análise do Balanço Patrimonial",
    "Análise do Fluxo de Caixa",
    "Análise de Tendências",
    "Análise de Receita e Lucro",
    "Análise de Posição de Mercado"
]

st.title('Gerador de Relatório Financeiro')

empresa = st.selectbox('Selecione a empresa:', companies)
quarter = st.selectbox('Selecione o trimestre:', quarters)
year = st.selectbox('Selecione o ano:', years)
period = f"{quarter} {year}"
language = st.selectbox('Selecione o idioma:', languages)
analysis = st.selectbox('Selecione a análise:', analysis)

if st.button('Gerar Relatório'):
    prompt = prompt_template.format(
        empresa=empresa,
        period=period,
        language=language,
        analysis=analysis
    )

    response = openai.invoke(prompt)

    st.subheader('Relatório Gerado:')
    st.write(response.content)
