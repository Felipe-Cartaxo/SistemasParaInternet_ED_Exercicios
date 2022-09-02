from Aluno import Aluno

aluno1 = Aluno(20221370005, 'Felipe Cartaxo', [8, 9, 7.5, 4]) # Testando se o objeto foi devidamente criado
print(aluno1) # Testando o método str

print(aluno1.notas) # Imprimindo as notas do aluno1
print(aluno1.calcMedia(aluno1.notas)) # Testando o método 'calcMedia'

aluno1.nome = 'Fefê Houston' # Testando o método modificador na propriedade privada 'nome'

aluno1.addNotas(0) # Testando o método 'addNotas'
print(aluno1.notas)
print(aluno1.calcMedia(aluno1.notas)) # Testando o método 'calcMedia'
print(aluno1) # Exibindo o objeto 'aluno1' após os métodos 'calcMedia' e 'addNotas'