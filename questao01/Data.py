'''
Implemente uma classe chamada Data, que poderá ser usada para representar uma data.
A classe deverá ter:

a) os atributos privados: dia, mês e ano, do tipo int.;
b) Construtor;
c) Métodos acessadores e modificadores;
d) Método __str__(self), que devera retornar a data no formato dd/mm/aaaa (String).

Escreva um programa para criar objetos dessa classe e testar os métodos.
'''

class Data: # Criação da classe 'Data'
    def __init__(self, dia:int, mes:int, ano:int): # Construtor de 'Data'
        self.__dia = dia # Atributo privado 'dia'
        self.__mes = mes # Atributo privado 'mês'
        self.__ano = ano # Atributo privado 'ano'

    def __str__(self): # Método str
        return f'{self.__dia}/{self.__mes}/{self.__ano}' # Impressão da data no formato dd/mm/aa

    @property
    def dia (self):
        return self.__dia # Método acessor para acessar a propriedade privada 'dia'

    @property    
    def mes (self):
        return self.__mes # Método acessor para acessar a propriedade privada 'mes'

    @property    
    def ano (self):
        return self.__ano # Método acessor para acessar a propriedade privada 'ano'

    @dia.setter
    def dia(self, novoDia):
        self.__dia = novoDia # Método modificador para alterar o valor da propriedade privada 'dia'

    @mes.setter
    def mes(self, novoMes):
        self.__mes = novoMes # Método modificador para alterar o valor da propriedade privada 'mes'
    
    @ano.setter
    def ano(self, novoAno):
        self.__ano = novoAno # Método modificador para alterar o valor da propriedade privada 'ano'