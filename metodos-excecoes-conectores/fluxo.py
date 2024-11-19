# Como estamos utilizando o alias conector no import, para trocar de banco de dados, bastaria apenas alterar o import da primeira linha. 
# Isso porque todas elas seguem a especificação DB-API 2.0.


# SQLite

import sqlite3 as conector

# Abertura de conexão
conexao = conector.connect("URL SQLite")

# Aquisição de um cursor
cursor = conexao.cursor()

# Execução comandos: SELECT..CREATE...
cursor.execute("...")
cursor.fetchall()

# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()

############################################

# MySQL

import mysql.connector as conector

# Abertura de conexão
conexao = conector.connect("URL MySQL")

# Aquisição de um cursor
cursor = conexao.cursor()

# Execução comandos: SELECT..CREATE...
cursor.execute("...")
cursor.fetchall()

# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()

#################################################

# PostgreSQL

import psycopg2 as conector

# Abertura de conexão
conexao = conector.connect("URL PostgreSQL")

# Aquisição de um cursor
cursor = conexao.cursor()

# Execução comandos: SELECT..CREATE...
cursor.execute("...")
cursor.fetchall()

# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()
