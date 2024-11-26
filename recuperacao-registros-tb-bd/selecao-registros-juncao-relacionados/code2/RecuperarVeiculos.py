from PessoaMarcaVeiculo import Veiculo, Marca

# Essa função tem como parâmetro uma conexão e o CPF de uma pessoa
# Esse CPF será utilizado para filtrar os veículos que ela possui. 
# Para isso, utilizamos o delimitador “?” 
# passamos o cpf da pessoa como argumento para o comando


def recuperar_veiculos(conexao, cpf):
    # Aquisição de cursor
    cursor = conexao.cursor()

    # Definição dos comandos
    comando = '''SELECT * FROM Veiculo
                 JOIN Marca ON Marca.id = Veiculo.marca
                 WHERE Veiculo.proprietario = ?;'''
    cursor.execute(comando, (cpf,))

    # Recuperação dos registros
    veiculos = [] # Essa lista será povoada com os veículos recuperados pela consulta ao longo do laço for
    registros = cursor.fetchall()
    for registro in registros:
        marca = Marca(*registro[6:])
        veiculo = Veiculo(*registro[:5], marca)
        veiculos.append(veiculo)

# Fechamento do cursor
    cursor.close()
    return veiculos