# inserir o seguinte registro na tabela Pessoa:

# CPF: 12345678900
# Nome: João
# Data de nascimento: 31/01/2000
# Usa óculos: Sim (True)

import sqlite3 as conector

 # Abertura de conexão e aquisição de cursor
conexao = conector.connect("insercao-remocao-atualizacao-dados-tb-bd\\insercao-dados\\meu_banco.db")
cursor = conexao.cursor()

# Execução de um comando: SELECT... CREATE ...
comando = ''' INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
                VALUES (12345678900, 'Joao', '2004-12-23', 1);'''

cursor.execute(comando)

# Efetivação do comando
conexao.commit()

# Fechamento das conexões
conexao.close
cursor.close