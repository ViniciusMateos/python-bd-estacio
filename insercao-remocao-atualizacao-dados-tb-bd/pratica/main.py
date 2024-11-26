from pratica import inserir_dados, conectar_banco, criar_tabelas

if __name__ == '__main__':
    conexao = conectar_banco("insercao-remocao-atualizacao-dados-tb-bd\\pratica\\ecommerce.db")
    criar_tabelas(conexao)
    inserir_dados(conexao)
    conexao.close()