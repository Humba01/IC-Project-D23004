# Importando Bibliotecas
import os
import datetime
import time
import sqlite3

# Declarando variáveis
umidade = 0
temperatura = 0
qualidade = 0
parametros = []

tempo = time.gmtime();

parar_leitura = True or False;

# Funções para coletar dados
def ler_umidade(coleta_manual_dados: bool):
  if coleta_manual_dados:
    umidade = input("Digite a umidade encontrada: ");
  else:
    umidade = 0; 
  return umidade;

def ler_temperatura(coleta_manual_dados: bool):
  if coleta_manual_dados:
    temperatura = input("Digite a temperatura encontrada: ");
  else:
    temperatura = 0;
  return temperatura;

def determina_qualidade(coleta_manual_dados: bool):
  if coleta_manual_dados:
    qualidade = input("Digite a qualidade do alimento encontrada (Suposição):");
  else:
    qualidade = 0;
  return qualidade;

def verifica_parametros():
  parametros = [umidade, temperatura, qualidade];
  print(parametros);

# Invocação das Funções
ler_umidade(True);
ler_temperatura(True);
determina_qualidade(True);
verifica_parametros();

# Informa a versão do SQLite 
print(sqlite3.version);

# Cria a conexão com o banco de dados
conn = sqlite3.connect('d23004.db');

# gera um cursor para manipulação do banco de dados
cursor = conn.cursor();

# Cria a tabela
cursor.execute("""
  CREATE TABLE IF NOT EXISTS dados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_hora DATETIME,
    umidade INTEGER,
    temperatura INTEGER,
    qualidade INTEGER
  )
""");

# Insere os dados na tabela
cursor.execute("""
  INSERT INTO dados (data_hora, umidade, temperatura, qualidade)
  VALUES (?, ?, ?, ?)
""", (datetime.datetime.now(), umidade, temperatura, qualidade));

# Salva as alterações
conn.commit();

# Fecha a conexão
conn.close();

# Cria uma cópia do banco de dados
os.system("cp d23004.db db/d23004_backup.db");

# Gera um arquivo de log
log = open("log.txt", "a");
log.write("\n" + str(datetime.datetime.now()) + " - Backup realizado com sucesso!");
log.close();

# Fecha o programa
exit()

