import socket
import sys
 
HOST = ''  
PORT = 8000
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print 'Socket created'
 
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
s.listen(10)
print 'Socket now listening'
 
#while 1:
conn, addr = s.accept()
print 'Connected with host ' + addr[0] + ':' + str(addr[1])
conn.send("0")
conn2, addr2 = s.accept()
print 'Connected with partner ' + addr2[0] + ':' + str(addr2[1])
conn2.send("1")
conn2.send(addr2[0])
s.close()