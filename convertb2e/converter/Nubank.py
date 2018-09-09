#coding: utf-8

'''

Classe que processa arquivo do Nubank

'''

from  Account import Account

class Nubank(Account):
    def __init__(self,fileName):
        super().__init__(fileName)

    def parse(self):
        print(self.texts)



if __name__ == '__main__':
    print("testes")
    account = Nubank("nubank.pdf")
    account.parse()
