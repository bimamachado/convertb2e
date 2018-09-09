#coding: utf-8

'''

Classe para criar em excel para Organizze

'''
import xlwt
from xlwt import Workbook
from ExcelObj import ExcelObj

class CreateExcel(object):

    def __init__(self):
        pass

    def generate(self,results,fileName):
        wb = Workbook()
        sheet1 = wb.add_sheet('Dados exportados do Organizze')
        sheet1.write(0,0,'Data')
        sheet1.write(0,1,'Descrição')
        sheet1.write(0,2,'Categoria')
        sheet1.write(0,3,'Valor')
        sheet1.write(0,4,'Situação')
        i=1
        for obj in results:
            sheet1.write(i,0,obj.data)
            sheet1.write(i,1,obj.descricao)
            sheet1.write(i,2,obj.categoria)
            sheet1.write(i,3,obj.valor)
            sheet1.write(i,4,obj.situacao)
            i+=1
        wb.save(fileName)




if __name__ == '__main__':
    excel = CreateExcel()
    dado = ExcelObj('01/02/2018','cambuca','restaurante',-3,'qualquer')
    list =[dado]
    excel.generate(list,'teste.xls')
