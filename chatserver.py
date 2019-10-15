#!/usr/bin/python
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

def clientthread(conn,addr):
    nick=conn.recv(2048).decode('utf-8')
    regex = re.compile('[@!#$%^&*()?/|}{~:]')
    if(regex.search(nick) == None) and len(nick)<=12:
        conn.sendall('<OK>'.encode('utf-8'))
    	
    else:
        conn.sendall('<ERR>'.encode('utf-8'))
        clients.remove(conn)
        sys.exit()

    while True:
        try:
            message = conn.recv(2048).decode('utf-8')
            
            if not message:
            	conn.close()
            	break 
            else:


            	if len(message)<=256 :
                	print('<'+nick+'>' + message)

                	message_to_send = message
                	broadcasting(message_to_send,conn,nick)
            	else:
                	clients.remove(conn)

        except KeyboardInterrupt: 
            break
            conn.close()


def broadcasting(message,connection,nick):
    for sockets in clients:
        if sockets != connection and socket!= server:
            try:
                sockets.sendall('<'+ nick +'>' + message.encode('utf-8'))
                    
            except KeyboardInterrupt:
                clients.remove(sockets)
                break 


while True:
    conn,addr=server.accept()
    conn.sendall('Hello Version 1'.encode('utf-8'))
    clients.append(conn)
    print(addr[0]+":connected")


    start_new_thread(clientthread,(conn,addr))

conn.close()
server.close()     





