#coding: utf-8
'''
Classe mae que define os método que devem ser implementados
pelas classes de cartão e banco
'''

import abc
from convertb2e.reader.PdfReader import PdfReader

class Account(object):


    def __init__(self,fileName):
        try:
            pdf = PdfReader()
            self.texts = pdf.extract2Text(fileName)
        except FileNotFoundError:
            print("Arquivo não encontrado")
    '''
     Método que será implementado para cada tipo de conta
    '''
    @abc.abstractmethod
    def parser(self):
        pass
