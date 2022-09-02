'''
Implemente uma classe chamada Aluno que deve ter:

a) Atributo matricula, do tipo int; nome, do tipo String; notas do tipo list;
b) Construtor para inicializar todos os atributos;
c) Métodos acessadores get_nome(self) e get_matricula(self). Este ultimo deve retornar a
matrícula como uma String formatada. Use o operador % (resto da divisão) para desmembrar os caracteres numéricos que compõem a matrícula;
d) Método media(self) que retorna a media das notas;
e) Método alterador apenas para o nome, set_nome(self)
f) Método adiciona_nota(self,nota),para adicionar uma nota à lista de notas, do aluno.
'''

class Aluno(): # Criação da classe 'Aluno'
    def __init__(self, matricula:int, nome:str, notas:list): # Construtor de 'Aluno'
        self.__matricula = matricula # Atributo privado 'matricula'
        self.__nome = nome # Atributo privado 'nome'
        self.__notas = notas # Atributo privado 'notas'

    def __str__(self): # Método str
        return f'Matrícula do aluno: {self.__matricula}\nNome do aluno: {self.__nome}\nNotas do aluno: {self.__notas}'

    def calcMedia(self, listaNotas:list): # Método que retorna a media das notas
        notasTotal = 0
        for x in range(len(listaNotas)):
            notasTotal += listaNotas[x]
        
        notasMedia = notasTotal / (len(listaNotas))

        return f'A média de {self.__nome} é {notasMedia:.1f}.'

    def addNotas (self, novaLista:list): # Método que adiciona nota à lista de notas
        self.notas.append(novaLista)

    @property
    def matricula(self):
        return self.__matricula # Método acessor para acessar a propriedade privada 'matricula'

    @property
    def notas(self):
        return self.__notas # Método acessor para acessar a propriedade privada 'notas'

    @property
    def nome(self):
        return self.__nome # Método acessor para acessar a propriedade privada 'nome'

    @nome.setter
    def nome(self, novoNome):
        self.__nome = novoNome # Método modificador para alterar o valor da propriedade privada 'nome'