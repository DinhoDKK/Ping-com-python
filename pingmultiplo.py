import os #importar o modulo ou biblioteca
import time #importar o modulo ou biblioteca

with open('hosts.txt') as file: #Para leitura do arquivo externo
    dump = file.read() #Fazendo a leitura do arquivo
    dump = dump.splitlines() #Separando em linhas horizontais

for ip in dump:
    print("Verificando o ip: " , ip)
    print('-'*60)
    os.system('ping -n 2 {}' .format(ip)) #Realizando o comando system para pingar os ips do arquivo
    print("-" * 60)
    time.sleep(5)