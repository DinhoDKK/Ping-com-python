import os #Importa o modulo ou biblioteca os (integra os programas do S.O)

print("#" *60) #Imprimindo o #60 vezes
ip_ou_host = input("Digite o ip ou host a ser verificado: ") #Criamos uma variavel que vai receber o ip
print("-"*60) #Imprimindo o -60 vezes
os.system('ping -n 6 {}' .format(ip_ou_host)) # Chamando o system da biblioteca os - chamando o comando ping
# -n (numero de pacotes que serão enviados)
print("-"*60) #Imprimindo o -60 vezes