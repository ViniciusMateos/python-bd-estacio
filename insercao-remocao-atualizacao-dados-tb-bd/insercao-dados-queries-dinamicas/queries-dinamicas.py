import sqlite3 as conector
from Pessoa import Pessoa

# Abertura de conexão e aquisição de cursor
conexao = conector.connect("insercao-remocao-atualizacao-dados-tb-bd\\insercao-dados-queries-dinamicas\\meu_banco.db")
cursor = conexao.cursor()

# Criação de um objeto do tipo Pessoa
pessoa = Pessoa(12345678902, 'Vinicius', '2004-12-23', 0)

# Definição de um comando com query parameter
comando = 'INSERT INTO Pessoa (cpf, nome, nascimento, oculos) VALUES (?, ?, ?, ?)'
cursor.execute(comando, (pessoa.cpf, pessoa.nome, pessoa.data_nascimento, pessoa.usa_oculos))

# Efetivação do comando
conexao.commit()

# Fechamento das conexões
conexao.close()
cursor.close()