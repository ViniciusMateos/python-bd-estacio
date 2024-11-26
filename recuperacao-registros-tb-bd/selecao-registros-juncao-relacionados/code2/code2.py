import sqlite3 as conector
from PessoaMarcaVeiculo import Pessoa
from RecuperarVeiculos import recuperar_veiculos

# Abertura de conexão e aquisição de cursor
conexao = conector.connect(
    "recuperacao-registros-tb-bd\\selecao-registros-juncao-relacionados\\meu_banco.db")
cursor = conexao.cursor()

# Definição dos comandos
comando = '''SELECT * FROM Pessoa;'''
comando2 = '''INSERT INTO Pessoa VALUES (10000000099, "Vinicin", 0, 1)'''
cursor.execute(comando2)
cursor.execute(comando)

# Recuperação dos registros
pessoas = []
reg_pessoas = cursor.fetchall()
for reg_pessoa in reg_pessoas:
    pessoa = Pessoa(*reg_pessoa)
    pessoa.veiculos = recuperar_veiculos(conexao, pessoa.cpf)
    pessoas.append(pessoa)

for pessoa in pessoas:
    print(pessoa.nome)
    for veiculo in pessoa.veiculos:
        print('\t', veiculo.placa, veiculo.marca.nome)
 # Fechamento das conexões
cursor.close()
conexao.close()