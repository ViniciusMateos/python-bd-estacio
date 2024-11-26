from pratica import conectar_banco, exibir_pedidos, inserir_dados, criar_tabelas

if __name__ == '__main__':
    conexao = conectar_banco(
        'recuperacao-registros-tb-bd\\pratica\\livraria.bd')
    criar_tabelas(conexao)
    inserir_dados(conexao)
    exibir_pedidos(conexao)
    conexao.close()
