# et2602-nimy18-lab1
this project is based on tcp protocol
here we create a chat room which consists of a server to which multiple clients can connect.
we have 2 scripts chatserver and chatclient.
execution of chatserver: 
                        $cd <Directory_where_chatserver_is_present>
                        $python <filename> IP_address:port 
execution of chatclient:
                        $cd <Directory_where_chatclient_is_present>
                        $python <filename> IP_address:port nickname
                        
Note- client and server should be run in different terminals
     IP_address - 127.0.0.1 or local host if you are running server script on your own computer, make sure client connects to the same ip and port of the server
     nick name- can be anything which is less than 12 letters and no special characters allowed
     
     
     
