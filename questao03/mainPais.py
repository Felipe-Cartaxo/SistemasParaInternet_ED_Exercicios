from Pais import Pais

p1 = Pais('Brasil', 'Brasilia', 4000) # Testando se o objeto foi devidamente instanciado
p2 = Pais('Argentina','Buenos Aires', 2000) # Testando se o objeto foi devidamente instanciado

print(p1) # Testando o método str
print(p2) # Testando o método str

print(p1.__vizinhos) # Testando o método acessor na propriedade privada 'vizinhos' ***NÃO ESTÁ FUNCIONANDO
print(p2.__capital) # Testando o método acessor na propriedade privada 'dia'

p1.addPaisDeFronteira('Uruguai') # Testando o método 'addPaisDeFronteira' e adicionando um país à lista de fronteiras
p1.addPaisDeFronteira('Argentina') # Testando o método 'addPaisDeFronteira' e adicionando um país à lista de fronteiras
p1.addPaisDeFronteira('Paraguai') # Testando o método 'addPaisDeFronteira' e adicionando um país à lista de fronteiras
p1.addPaisDeFronteira('Peru') # Testando o método 'addPaisDeFronteira' e adicionando um país à lista de fronteiras
p1.addPaisDeFronteira('Peru') # Testando o método 'addPaisDeFronteira', adicionando um país à lista de fronteiras e verificando se países iguais serão adicionados à lista

print(p1.__vizinhos) # Exibindo a lista de países que fazem fronteira