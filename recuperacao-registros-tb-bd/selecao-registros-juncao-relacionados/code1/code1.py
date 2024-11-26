import sqlite3 as conector
from PessoaMarcaVeiculo import Veiculo, Marca

# Abertura de conexão e aquisição de cursor
conexao = conector.connect("recuperacao-registros-tb-bd\\selecao-registros-juncao-relacionados\\meu_banco.db")
cursor = conexao.cursor()

# Definição dos comandos
comando = '''SELECT * FROM
            Veiculo JOIN Marca ON Marca.id = Veiculo.marca;'''
cursor.execute(comando)

# Recuperação dos registros
registros = cursor.fetchall()
for registro in registros:
    print(registro)
    marca = Marca(*registro[6:]) #array slice para selecionar apenas os atributos da Marca
                                #Essa tupla é utilizada em conjunto com o operador * para criar um objeto do tipo Marca
                                # Como agora temos acesso ao id da Marca, foi necessário adicionar o id ao construtor da classe Marca.

    veiculo = Veiculo(*registro[:5], marca) # array slice para selecionar apenas os atributos do Veículo
                                            # removemos o id da Marca no slice
                                            # pois ele será substituído pelo objeto marca criado na linha 17.

    print("Placa:", veiculo.placa, ", Marca:", veiculo.marca.nome)

 # Fechamento das conexões
cursor.close()
conexao.close()
