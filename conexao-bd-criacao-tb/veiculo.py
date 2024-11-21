# - definir a entidade Veiculo, de forma que os atributos tenham os seguintes tipos e restrições:
#     placa: CHARACTER (chave primária, não nulo, tamanho 7).
#     ano: INTEGER (não nulo).
#     cor: TEXT (não nulo).
#     proprietario: INTEGER (chave estrangeira, não nulo)
#     marca: INTEGER (chave estrangeira, não nulo).

# nossas placas são compostas por 7 caracteres, nosso atributo placa terá tamanho 7 (CHAR(7) ou CHARACTER(7)). Por afinidade, ele será convertido para TEXT.

# atributo proprietário será utilizado para indicar um relacionamento da entidade Veículo com a entidade Pessoa

# atributo da tabela Pessoa utilizado no relacionamento será o CPF
# Como o CPF é um INTEGER, o atributo relacionado proprietario também precisa ser INTEGER.

# atributo marca será utilizado para indicar um relacionamento da entidade Veículo com a entidade Marca
# por meio do atributo id da tabela Marca, que também é um INTEGER.

import sqlite3 as conector

# Abertura de conexão e aquisição de cursor
conexao = conector.connect("conexao-bd-criacao-tb\\meu_banco.db")
cursor = conexao.cursor()

# Execução de um comando: SELECT... CREATE ...
comando = '''CREATE TABLE Veiculo (
                placa CHARACTER(7) NOT NULL,
                ano INTEGER NOT NULL,
                cor TEXT NOT NULL,
                proprietario INTEGER NOT NULL,
                marca INTEGER NOT NULL,
                PRIMARY KEY (placa),
                FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
                FOREIGN KEY(marca) REFERENCES Marca(id)
                );'''

cursor.execute(comando)

# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()
