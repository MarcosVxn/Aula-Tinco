import socket #biblioteca
import time #biblioteca

HOST = "127.0.0.1" #endereço do servidor
PORT = 5000 #porta que o servidor esta utilizando
tcp = socket. socket (socket.AF_INET, socket. SOCK_STREAM) #Instan. TCP familia IPv4
dest = (HOST, PORT)
tcp.connect (dest) #conexao via tcp

print("-----------------------------------------------------------------------------------")
print("A - Um contador do 0 á 20")
print("B - A impressão na tela do nome da Faculdade SENAI Antonio Adolpho Lobbe")
print("C - A tabuada do 7")
print("D - Os valores ímpares do intervalo 1 á 30")
print("-----------------------------------------------------------------------------------")


while True:

    Requiopcao = input('Qual das função sera executada? ')
    
    match Requiopcao:
        case "A":
            for cont in (range (21)):
                print(cont)
            
                
        case "B":
            print("Faculdade de Tecnologia e Escola SENAI Antonio Adolpho Lobbe")

            
        case "C":
            for i in range (11):
                resu = i * 7
                print(f"7 x {i} = {resu}")
        

        case "D":
            for i in range (1, 31, 2):
                print (i)
        

    tcp.send(Requiopcao.encode('utf-8')) #enviando a mensagem
    time.sleep(1) #tempo para envio da mensagem
