import sqlite3
from gerenciamento_livraria import Cliente, Livro, Pedido

def conectar_banco(nome_banco):
    conexao = sqlite3.connect(nome_banco)
    return conexao

def criar_tabelas(conexao):
    cursor = conexao.cursor()
   
    cursor.execute('''CREATE TABLE IF NOT EXISTS Livros (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      titulo TEXT NOT NULL,
                      autor TEXT NOT NULL,
                      preco REAL NOT NULL)''')
   
    cursor.execute('''CREATE TABLE IF NOT EXISTS Clientes (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      nome TEXT NOT NULL,
                      email TEXT NOT NULL)''')
   
    cursor.execute('''CREATE TABLE IF NOT EXISTS Pedidos (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      cliente_id INTEGER NOT NULL,
                      livro_id INTEGER NOT NULL,
                      quantidade INTEGER NOT NULL,
                      data_pedido TEXT NOT NULL,
                      FOREIGN KEY (cliente_id) REFERENCES Clientes(id),
                      FOREIGN KEY (livro_id) REFERENCES Livros(id))''')
   
    conexao.commit()

def inserir_dados(conexao):
    cursor = conexao.cursor()    

    livros = [Livro('Python para Iniciantes', 'John Doe', 39.99),
              Livro('Algoritmos e Estruturas de Dados', 'Jane Smith', 49.99),
              Livro('Inteligência Artificial', 'Alan Turing', 59.99)]    

    clientes = [Cliente('Alice', 'alice@example.com'),
                Cliente('Bob', 'bob@example.com'),
                Cliente('Charlie', 'charlie@example.com')]    

    pedidos = [Pedido(1, 1, 2, '2023-06-15'),
               Pedido(2, 2, 1, '2023-06-16'),
               Pedido(3, 3, 3, '2023-06-17')]    

    for livro in livros:
        cursor.execute('INSERT INTO Livros (titulo, autor, preco) VALUES (:titulo, :autor, :preco)', vars(livro))    
        
    for cliente in clientes:
        cursor.execute('INSERT INTO Clientes (nome, email) VALUES (:nome, :email)', vars(cliente))  
          
    for pedido in pedidos:
        cursor.execute('INSERT INTO Pedidos (cliente_id, livro_id, quantidade, data_pedido) VALUES (:cliente_id, :livro_id, :quantidade, :data_pedido)', vars(pedido))    
    conexao.commit()


def exibir_pedidos(conexao):
    cursor = conexao.cursor()   
    query = '''    
    SELECT Pedidos.id, Clientes.nome, Livros.titulo, Pedidos.quantidade, Pedidos.data_pedido
    FROM Pedidos
    JOIN Clientes ON Pedidos.cliente_id = Clientes.id
    JOIN Livros ON Pedidos.livro_id = Livros.id
    '''    
    cursor.execute(query)
    pedidos = cursor.fetchall()    
    print('Pedidos:')

    for pedido in pedidos:        
        print(pedido)

def exibir_pedidos(conexao):
    cursor = conexao.cursor()   
    query = '''    
    SELECT Pedidos.id, Clientes.nome, Livros.titulo, Pedidos.quantidade, Pedidos.data_pedido
    FROM Pedidos
    JOIN Clientes ON Pedidos.cliente_id = Clientes.id
    JOIN Livros ON Pedidos.livro_id = Livros.id
    '''    
    cursor.execute(query)
    pedidos = cursor.fetchall()    
    print('Pedidos:')

    for pedido in pedidos:        
        print(pedido)