# - Em algumas situações, as colunas precisam seguir uma ordem específica
# - Um cenário comum é quando carregamos dados de uma planilha diretamente para um banco de dados, para fazer uma inserção em massa (bulk insert)
# - Nesses casos, as colunas da planilha devem estar na mesma ordem das colunas do banco.

# - Como nem todos os bancos de dados, incluindo o SQLite, dão suporte à criação de colunas em posição determinada, vamos precisar remover nossa tabela para recriá-la com os atributos na posição desejada.
# - Para o nosso exemplo, desejamos esta sequência:
#     Placa
#     Ano
#     Cor
#     Motor
#     Proprietário
#     Marca

# - No exemplo a seguir, vamos remover a tabela Veículo, utilizando o comando DROP TABLE do SQL e, posteriormente, vamos criá-la novamente com a sequência desejada.

import sqlite3 as conector

# Abertura de conexão e aquisição de cursor
conexao = conector.connect("conexao-bd-criacao-tb\\meu_banco.db")
cursor = conexao.cursor()

# Execução de um comando: SELECT... CREATE ...
comando1 = '''DROP TABLE Veiculo;'''

cursor.execute(comando1)

comando2 = '''CREATE TABLE Veiculo (
               placa CHARACTER(7) NOT NULL,
                ano INTEGER NOT NULL,
               cor TEXT NOT NULL,
                motor REAL NOT NULL,
               proprietario INTEGER NOT NULL,
                marca INTEGER NOT NULL,
               PRIMARY KEY (placa),
                FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
               FOREIGN KEY(marca) REFERENCES Marca(id)
                );'''

cursor.execute(comando2)

# Efetivação do comando
conexao.commit()

 # Fechamento das conexões
cursor.close()
conexao.close()
