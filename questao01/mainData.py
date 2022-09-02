from Data import Data

data1 = Data(1,9,2022) # Testando se o objeto foi devidamente instanciado
print(data1) # Testando o método str
print(data1.dia) # Testando o método acessor na propriedade privada 'dia'
print(data1.mes) # Testando o método acessor na propriedade privada 'mes'
print(data1.ano) # Testando o método acessor na propriedade privada 'ano'

data1.dia = 99 # Testando se método modificador alterou a propriedade privada 'dia'
data1.mes = 9 # Testando se método modificador alterou a propriedade privada 'mes'
data1.ano = 9999 # Testando se método modificador alterou a propriedade privada 'ano'

print(data1) # Testando se o método modificador alterou o objeto
print(data1.dia) # Testando a variável 'dia' após a alteração pelo método modificador
print(data1.mes) # Testando a variável 'mes' após a alteração pelo método modificador
print(data1.ano) # Testando a variável 'ano' após a alteração pelo método modificador