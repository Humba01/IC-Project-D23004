from curses import echo
import datetime
import time
import sqlite3

umidade = 0
temperatura = 0
qualidade = 0
parametros = []

tempo = time.gmtime();

datetime.time(tempo);

parar_leitura = True or False;

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
  echo(parametros);

ler_umidade(True);
ler_temperatura(True);
determina_qualidade(True);
verifica_parametros();

# K Informa a versão do SQLite 
sqlite3.sqlite_version_info();

sqlite3.connect('d23004.db');


