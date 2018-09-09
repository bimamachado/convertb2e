'''
Classe que representa o resutado esperado pelo excel
'''

class ExcelObj(object):

    def __init__(self,data,descricao, categoria,valor, situacao):
        self.data = data
        self.descricao =  descricao
        self.categoria = categoria
        self.valor     =  valor
        self.situacao  =  situacao