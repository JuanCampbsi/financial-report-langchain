import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from config.connect import initialize
from template.analysis_financial_class import AnalysisFinancial
from data.arrays import companies, quarters, years, languages, analysis

initialize()
openai = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0)
template = AnalysisFinancial()

#Format Markdown
prompt_template = PromptTemplate.from_template(template=template.model)

st.title('Gerador de Relatório Financeiro')

empresa = st.sidebar.selectbox('Selecione a empresa:', companies)
quarter = st.sidebar.selectbox('Selecione o trimestre:', quarters)
year = st.sidebar.selectbox('Selecione o ano:', years)
period = f"{quarter} {year}"
language = st.sidebar.selectbox('Selecione o idioma:', languages)
analysis = st.sidebar.selectbox('Selecione a análise:', analysis)

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
