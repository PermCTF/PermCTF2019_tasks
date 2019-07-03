import socket
import threading
import random 
import string
import time 

bind_ip = "0.0.0.0"
bind_port = 1337

server = socket.socket()
server.bind((bind_ip,bind_port))
server.listen(5)
print(f"[*] Listening on {bind_ip}:{bind_port}")

# this is our client-handling thread
def handle_client(client_socket):
   
    ERR_MSG = 'Ты где-то ошибся :('
    SUCC_MSG = 'Атлишна. Держи флаг: PermCTF{w0w_s0ck3ts_4r3_4w3s0me}'
    SKIP_MSG = 'Давай пропустим этот треш :)'
   
    Score = random.randint(30,50) # wish you a good luck 
    alphabet = string.ascii_lowercase
   
    msg = '\nN-{}\nM-{}\nПожалуйста, отправь мне N букв M одним сообщением :] ({}/{})\n' 

    i = 0
    while i <  Score :
        number = random.randint( 10,20 )
        char = random.choice( alphabet )
       
        try:
            client_socket.send( msg.format(number,char,i,Score).encode()  )
            request = client_socket.recv( 1024 ).decode()
            print(f"[*] Received: { request }") 
        
            if request.strip()  == char*number: 
                i += 1
                continue
            else:
                if request != '\n':
                    client_socket.send( ERR_MSG.encode() )    
                else: client_socket.send( SKIP_MSG.encode() )
                i = 0
        except BrokenPipeError:
            pass            
    
    # Receive the FLAG
    client_socket.send( SUCC_MSG.encode() ) 

while True:
    try:
        client,addr = server.accept()
        print(f"[*] Accepted connection from: {addr[0]}{addr[1]}")
        client_handler = threading.Thread(target=handle_client,args=(client,))
        client_handler.start()
    except:
        break
