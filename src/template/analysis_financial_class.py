class AnalysisFinancial:
    def __init__(self):
          self.__template = '''
          Você é um analista financeiro.
          Escreva um relatório financeiro detalhado para a empresa "{empresa}" para o período {period}.

          O relatório deve ser escrito em {language} e incluir a seguinte análise:
          {analysis}

          Certifique-se de fornecer insights e conclusões para esta seção.
          '''
    @property
    def model(self):
      return self.__template 
          
  