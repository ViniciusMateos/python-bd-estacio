# - Assim como no comando INSERT, podemos montar o comando UPDATE de três formas
# - Uma string sem delimitadores, uma string com o delimitador “?” ou uma string com argumentos nomeados.

import sqlite3 as conector

# Abertura de conexão e aquisição de cursor
conexao = conector.connect("insercao-remocao-atualizacao-dados-tb-bd\\atualizacao-remocao-dados\\meu_banco.db")
conexao.execute("PRAGMA foreign_keys = on")
cursor = conexao.cursor()

# Definição dos comandos

# sem delimitadores
# atualizando o valor do atributo óculos para 1 (verdadeiro) para TODOS os registros da tabela.
# Isso ocorreu porque a cláusula WHERE foi omitida
comando1 = '''UPDATE Pessoa SET oculos= 1;'''
cursor.execute(comando1)

#com demilitadores
# comando de UPDATE utilizando o delimitador “?” para o valor do atributo óculos e explicitamos o valor do CPF na cláusula WHERE.
# Ou seja, vamos alterar o valor do atributo óculos para zero (falso) apenas para quem tem CPF igual a 30000000099.
comando2 = '''UPDATE Pessoa SET oculos= ? WHERE cpf=30000000099;'''
cursor.execute(comando2, (False,))

# argumentos nomeados
comando3 = '''UPDATE Pessoa SET oculos= :usa_oculos WHERE cpf= :cpf;'''
cursor.execute(comando3, {"usa_oculos": False, "cpf": 20000000099})


# Cuidado ao executar um comando UPDATE sem a cláusula WHERE, pois, dependendo do tamanho do banco de dados, essa operação pode ser muito custosa.


# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()