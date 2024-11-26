import sqlite3 as conector
from Pessoa import Pessoa
from Marca import Marca
from Veiculo import Veiculo

# Abertura de conexão e aquisição de cursor
conexao = conector.connect("insercao-remocao-atualizacao-dados-tb-bd\\insercao-dados-queries-dinamicas-nomes\\meu_banco.db")
cursor = conexao.cursor()

# Criação de um objeto do tipo Pessoa
pessoa = Pessoa(20000000092, 'Vinicius', '1990-02-28', False)

# Definição de um comando com query parameter
comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
                    VALUES (:cpf,:nome,:data_nascimento,:usa_oculos);'''
cursor.execute(comando, {"cpf": pessoa.cpf,
                        "nome": pessoa.nome,
                        "data_nascimento": pessoa.data_nascimento,
                        "usa_oculos": pessoa.usa_oculos})



# código está crescendo
# Imagine se tivéssemos uma entidade com dezenas de atributos? 
# A chamada do método execute da linha 14 cresceria proporcionalmente, comprometendo muito a leitura do nosso código.

# Quando utilizamos o comando INSERT INTO do SQL para inserir um registro onde todos os atributos estão preenchidos, podemos suprimir o nome das colunas no comando.

# Como vamos inserir uma pessoa com todos os atributos, manteremos apenas os argumentos nomeados no comando SQL.

# vamos simplificar mais um pouco nosso código, removendo o nome das colunas no comando SQL e utilizando a função interna vars do Python que converte objetos em dicionários.


# Criação de um objeto do tipo Pessoa
pessoa = Pessoa(30000000092, 'Silva', '1990-03-30', True)

# Definição de um comando com named parameter
comando = '''INSERT INTO Pessoa VALUES (:cpf,:nome,:data_nascimento,:usa_oculos);'''
cursor.execute(comando, vars(pessoa))
print(vars(pessoa))

# Na linha 36, criamos o comando SQL INSERT INTO, no qual suprimimos o nome das colunas após o nome da tabela Pessoa
# Na linha 37, utilizamos o método execute passando como segundo argumento vars(pessoa)
# A função interna vars retorna todos os atributos de um objeto na forma de dicionário, no qual cada chave é o nome de um atributo.

# vamos inserir alguns registros nas outras tabelas para povoar nosso banco de dados
# utilizar a mesma lógica do exemplo anterior, no qual utilizamos a função vars() e argumentos nomeados

conexao.execute("PRAGMA foreign_keys = on")
# PRAGMA é uma extensão do SQL exclusiva do SQLite, usada para ajustar certos comportamentos internos do banco de dados.
# Por padrão, o SQLite não aplica a verificação de restrições de chave estrangeira. 
# Isso acontece por razões históricas, já que versões anteriores do SQLite não suportavam chaves estrangeiras.
# garantir que as restrições de chave estrangeiras sejam checadas antes de cada operação.



comandoMarca = '''INSERT INTO Marca (nome, sigla) VALUES (:nome, :sigla);'''

# Como não iremos passar um valor para o id da marca, que é autoincrementado, foi necessário explicitar o nome das colunas no comando INSERT INTO
# Caso omitíssemos o nome das colunas, seria gerada uma exceção do tipo OperationalError, com a descrição indicando que a tabela tem 3 colunas, mas apenas dois valores foram fornecidos
marca1 = Marca(1, "Citroen", "CT")
cursor.execute(comandoMarca, vars(marca1))
marca1.id = cursor.lastrowid # na criação do objeto marca1 é passado um valor de Id para nao ter a exceção ja mencionada, esse comando serve para passar o novo valor do atributo ID, fazendo-o se tornar autoincrementavel

marca2 = Marca(2, "Volks", "VK")
cursor.execute(comandoMarca, vars(marca2))
marca2.id = cursor.lastrowid

# Como vamos inserir um veículo com todos os atributos, omitimos os nomes das colunas.
comandoVeiculo = '''INSERT INTO Veiculo VALUES (:placa, :ano, :cor, :motor, :proprietario, :marca);'''

# Para criar uma referência da marca que acabamos de inserir em um veículo, precisamos do id autoincrementado gerado pelo banco no momento da inserção.
# Para isso, vamos utilizar o atributo lastrowid do Cursor
# Esse atributo armazena o id da linha do último registro inserido no banco e está disponível assim que chamamos o método execute do Cursor
# O id da linha é o mesmo utilizado para o campo autoincrementado.

veiculo1 = Veiculo(12345, 2005, "Marrom", 1.0, 10000000099, marca2.id)
veiculo2 = Veiculo(12341, 2005, "Marrom", 2.0, 10000000099, marca2.id)
veiculo3 = Veiculo(12342, 2005, "Marrom", 3.0, 10000000099, marca1.id)
veiculo4 = Veiculo(12343, 2005, "Marrom", 4.0, 10000000099, marca1.id)

#Lembre-se de que como os atributos proprietário e marca são referências a chaves de outras tabelas, eles precisam existir no banco!
# Caso contrário, será lançada uma exceção de erro de integridade (IntegrityError) com a mensagem “Falha na restrição de chave estrangeira (FOREIGN KEY constraint failed)”.



cursor.execute(comandoVeiculo, vars(veiculo1))
cursor.execute(comandoVeiculo, vars(veiculo2))
cursor.execute(comandoVeiculo, vars(veiculo3))
cursor.execute(comandoVeiculo, vars(veiculo4))

# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()