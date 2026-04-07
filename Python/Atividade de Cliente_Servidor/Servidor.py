import socket #biblioteca

HOST = "127.0.0.1" #endereco do servidor
PORT = 5000 #porta que o servidor irá ficar ouvindo a rede

tcp = socket. socket (socket.AF_INET, socket. SOCK_STREAM) #Instan. TCP familia IPv4
orig = (HOST, PORT)

tcp.bind(orig) #Passagem do endereço e porta
tcp.listen (1) #Quantidade de conexões

while True: #Loop
    print ('Aguardando conexao') #mensagem para orientaçao
    
    con , cliente = tcp.accept () #aguardando o aceite da conexão
    print ('Conectado por:', cliente) #mensagem de conexão
    
    while True: #loop de recebimento de mensagens
        Requiopcao = con.recv (1024) #variavel onde sera recebida a mensagem
    
        if not Requiopcao: #verifica se ha mensagem
            break #se nao houver mensagem sai do loop
    
        print (cliente, Requiopcao) #impressao da mensagem recebida
            
    print ('Finalizando conexão do cliente', cliente) #mensagem de orientaçao
    con.close () #finalizaçao da conexao
