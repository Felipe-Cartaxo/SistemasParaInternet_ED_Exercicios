'''
Escreva uma classe que represente um país. Um país tem como atributos privados o seu nome,
o nome da capital, sua dimensão em Km2 e uma lista de países com os quais ele faz
fronteira. Represente a classe e forneça os seguintes construtores e método:

a) Construtor que inicialize o nome, capital e a dimensão do país;
b) Métodos de acesso para os atributos indicados no item (a);
c) Método que retorne a lista de países que fazem fronteira;
d) Método que adiciona o nome de país à lista de fronteiras (verificar se o nome já existe na lista);
e) Método __str__(self).
'''

from typing import List

class Pais: # Criação da classe 'Pais'
    def __init__(self, nome:str, capital:str, dimensao:int): # Construtor de 'Pais'
        self.__nome = nome # Atributo privado 'nome'
        self.__capital = capital # Atributo privado 'capital'
        self.__dimensao = dimensao # Atributo privado 'dimensao'
        self.__vizinhos = List() # Atributo privado 'vizinhos'
    
    def __str__(self): #Método str
        return f'{self.__nome}, capital {self.__capital}, {self.__dimensao} Km²' #

    @property
    def nome(self):
        return self.__nome # Método acessor para acessar a propriedade privada 'nome'

    @property
    def capital(self):
        return self.__capital # Método acessor para acessar a propriedade privada 'capital'

    @property
    def dimensao(self):
        return self.__dimensao # Método acessor para acessar a propriedade privada 'dimensao'

    @property
    def vizinhos(self):
        return self.__vizinhos # Método acessor para acessar a propriedade privada 'vizinhos'

    def addPaisDeFronteira(self, nome_do_pais:str): # Método que adiciona o nome de país à lista de fronteiras
        if nome_do_pais not in self.__vizinhos:
            self.__vizinhos.append(nome_do_pais)