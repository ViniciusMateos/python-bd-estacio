import sqlite3 as conector

conexao = conector.connect("recuperacao-registros-tb-bd\\recuperando-registros\\meu_banco.db")
cursor = conexao.cursor()

comando = '''SELECT nome, oculos FROM Pessoa;''' # selecionando todas as pessoas da tabela, visto que não há cláusulas WHERE
cursor.execute(comando)

registros = cursor.fetchall() # método fetchall do cursor para recuperar os registros selecionados.

print("Tipo retornado pelo fetchall():", type(registros)) # objeto retornado pelo método fetchall é do tipo lista

for registro in registros:
    print("Tipo: ", type(registro), "- Conteudo: ", registro)
    # Os registros são sempre retornados em forma de tupla, mesmo que contenham apenas um atributo.

# Como o SQLite não cria uma transação para o comando SELECT, não é necessário executar o commit.

#################################################################

# agora uma consulta para retornar às pessoas que usam óculos

print()

from Pessoa import Pessoa


comando = '''SELECT * FROM Pessoa WHERE oculos=:usa_oculos;''' # apenas as pessoas que usam oculos
# utilizamos o asterisco (*) para representar quais dados desejamos receber
cursor.execute(comando, {"usa_oculos": True})

registros = cursor.fetchall()

for registro in registros:
    pessoa = Pessoa(*registro) # Foi utilizado o operador * do Python. Esse operador “desempacota” um iterável, passando cada elemento como um argumento para uma função ou construtor.
    # Como sabemos que a ordem das colunas é a mesma ordem dos parâmetros do construtor da classe Pessoa, garantimos que vai funcionar corretamente.
    print("cpf:", type(pessoa.cpf), pessoa.cpf)
    print("nome:", type(pessoa.nome), pessoa.nome)
    print("nascimento:", type(pessoa.data_nascimento), pessoa.data_nascimento)
    print("oculos:", type(pessoa.usa_oculos), pessoa.usa_oculos)
    print()


cursor.close()
conexao.close()