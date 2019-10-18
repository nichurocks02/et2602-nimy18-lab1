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
nick=str(sys.argv[2])

server.connect((IP_addr, port))

first_msg=server.recv(2048).decode('utf-8')

print(first_msg)



#print('NICK '+nick.encode('utf-8'))

server.sendall('NICK '+nick.encode('utf-8'))

ok_msg=server.recv(2048).decode('utf-8')
print(ok_msg)
if ok_msg == "OK":
    pass
elif ok_msg == "ERROR":
    print('do not enter nick name with special characters')
    print('sorry you are disconnected')
    sys.exit()
    



while True:
    socket_list=[sys.stdin, server]
    ''' here either user wants to give an input to send to other people or server is sending a msg to us to be displayed on the terminal. '''

    read_sockets,write_sockets,error_sockets=select.select(socket_list,[],[])
    '''def select(rlist, wlist, xlist, timeout)
Wait until one or more file descriptors are ready for some kind of I/O. The first three arguments are sequences of file descriptors to be waited for: rlist -- wait until ready for reading wlist -- wait until ready for writing xlist -- wait for an `exceptional condition'' If only one kind of condition is required, pass [] for the other lists. A file descriptor is either a socket or file object, or a small integer gotten from a fileno() method call on one of those.

The optional 4th argument specifies a timeout in seconds; it may be a floating point number to specify fractions of seconds. If it is absent or None, the call will never time out.

The return value is a tuple of three lists corresponding to the first three arguments; each contains the subset of the corresponding file descriptors that are ready.

'''
    for sockets in read_sockets:
        if sockets == server:
            message = sockets.recv(2048).decode('utf-8')
            print(message)
        else:
            message=sys.stdin.readline()
            if message == '\n':
                continue
            else:
                server.sendall(message[:-1].encode('utf-8'))
server.close()



