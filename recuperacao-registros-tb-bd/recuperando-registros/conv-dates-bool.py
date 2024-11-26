# O conector sqlite3 permite realizar essa conversão automaticamente, mas exige algumas configurações adicionais.
# como fazer a conversão de datas e booleanos.

import sqlite3 as conector
from Pessoa import Pessoa

# Abertura de conexão e aquisição de cursor
conexao = conector.connect("recuperacao-registros-tb-bd\\recuperando-registros\\meu_banco.db", detect_types=conector.PARSE_DECLTYPES) # o conector deve tentar fazer uma conversão dos dados, tomando como base o tipo da coluna declarada no CREATE TABLE.
cursor = conexao.cursor()

# tipos DATE e TIMESTAMP já possuem conversores embutidos no sqlite3, porém o tipo BOOLEAN não
# Para informar ao conector como fazer a conversão do tipo BOOLEAN, precisamos definir e registrar a função conversora utilizando a função interna register_converter do sqlite3.


# Funções conversoras
def conv_bool(dado):
    return True if dado == 1 else False

# Registro de conversores
conector.register_converter("BOOLEAN", conv_bool)

# Definição dos comandos
comando = '''SELECT * FROM Pessoa WHERE oculos=:usa_oculos;'''
cursor.execute(comando, {"usa_oculos": True})

# Recuperação dos registros
registros = cursor.fetchall()
for registro in registros:
    pessoa = Pessoa(*registro)
    print("cpf:", type(pessoa.cpf), pessoa.cpf)
    print("nome:", type(pessoa.nome), pessoa.nome)
    print("nascimento:", type(pessoa.data_nascimento), pessoa.data_nascimento)
    print("oculos:", type(pessoa.usa_oculos), pessoa.usa_oculos)

# Fechamento das conexões
cursor.close()
conexao.close()