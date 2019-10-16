#!/usr/bin/python3
import socket
import sys
from _thread import *
import select 
import re 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


Info = (sys.argv[1])
a=Info.split(':')
IP_addr=str(a[0])
port=int(a[1])

server.bind((IP_addr,port))

server.listen(100)


clients=[]
clients.append(server)

def clientthread(conn,addr):
    nick=conn.recv(2048).decode('utf-8')
    nick1=nick.strip('NICK ')
    regex = re.compile('[@!#$%^&*()?/|}{~:]')
    if(regex.search(nick1) == None) and len(nick1)<=12:
        conn.sendall('OK'.encode('utf-8'))
    	
    else:
        conn.sendall('ERROR'.encode('utf-8'))
        clients.remove(conn)
        sys.exit()

    while True:
        try:
            message = conn.recv(2048).decode('utf-8')
            message1=message.strip('MSG')

            
            if not message1:
            	conn.close()
                clients.remove(conn)
            	break 
            else:

                #a=re.compile('^[\x00-\x80]')
                if len(message1)<=255:
                    print('MSG ' + nick1 + message1)
                    message_to_send = 'MSG ' +''+nick1+'' + message1
                    broadcasting(message_to_send,conn,nick1)

            	elif len(message1) > 255 :
                    conn.sendall('ERROR'.encode('utf-8'))

        except KeyboardInterrupt: 
            conn.close()
            break

def broadcasting(message,connection,nick1):
    for sockets in clients:
        if sockets != connection and sockets!= server:
            try:
                sockets.sendall(message.encode('utf-8'))
            except KeyboardInterrupt:
                    clients.remove(sockets)
                    break 
while True:
    conn,addr=server.accept()
    conn.sendall('Hello 1'.encode('utf-8'))
    clients.append(conn)
    
    print(addr[0]+":connected")
    
    start_new_thread(clientthread,(conn,addr))


conn.close()
server.close()     





