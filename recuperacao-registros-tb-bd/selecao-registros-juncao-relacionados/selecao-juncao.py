# buscar registros em tabelas relacionadas
# buscar os veículos e suas respectivas marcas, utilizando junção de tabelas.

import sqlite3 as conector
from Veiculo import Veiculo

# Abertura de conexão e aquisição de cursor
conexao = conector.connect(
    "recuperacao-registros-tb-bd\\selecao-registros-juncao-relacionados\\meu_banco.db")
cursor = conexao.cursor()

# Definição dos comandos
comando = '''SELECT * FROM Veiculo;'''
cursor.execute(comando)

# Recuperação dos registros
reg_veiculos = cursor.fetchall()
for reg_veiculo in reg_veiculos:
    veiculo = Veiculo(*reg_veiculo) # objeto do tipo Veículo utilizando o operador * e imprimimos os atributos Placa e Marca
    print("Placa:", veiculo.placa, ", Marca:", veiculo.marca)

###############################################

# E se quisermos substituir o id das marcas pelos seus respectivos nomes?
# Para isso, precisamos realizar uma junção das tabelas Veículo e Marca no comando SELECT.

print()

comando = ''' SELECT Veiculo.placa, Veiculo.ano, Veiculo.cor, Veiculo.motor, Veiculo.proprietario, Marca.nome 
                FROM Veiculo 
                JOIN Marca ON Marca.id = Veiculo.marca;'''
cursor.execute(comando)

# Recuperação dos registros
reg_veiculos = cursor.fetchall()
for reg_veiculo in reg_veiculos:
    veiculo = Veiculo(*reg_veiculo)
    print("Placa:", veiculo.placa, ", Marca:", veiculo.marca)


# Fechamento das conexões
cursor.close()
conexao.close()
