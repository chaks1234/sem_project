import socket
import numpy as np
from test import *
from thread import *
#import matplotlib.pyplot as plt
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
################################################################

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]
################################################################

def threaded_client(conn):
    print('thread is running')
    del x[:]
    del y[:]
    data2 = 0.00
    i = 0
    while True:
        data = conn.recv(4048)
	try:
		data2 = float(data)
	except Exception: 
  		pass
        reply = 'Client:  '+data +'\n'
	if i < 50:
		x.append(i)
	if i >= 50:
		y.pop(0)
	y.append(data2)
	
	i = i + 1
        if not data:
            break
        print str(data2) + "		"+ str(i)
    conn.close()
    graph(x,y)
    print('thread closed\n')
##################################################################



host = get_ip_address()
port = 55009
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
plt.axis([0, 50, 0, 1])
plt.ion()
x = list()
y = list()


try:
    s.bind((host,port))
except socket.error as e:
    print(str(e))
s.listen(50)
print('IP address of server is  ' + host + ':' + str(port))
print('waiting for the connection')



while True:
    try:
        conn, addr = s.accept()
        print('connected to:' + addr[0] +':' + str(addr[1]))
        #print conn.recv(20)
        #start_new_thread(threaded_client,(conn,))
	threaded_client(conn)
	plt.cla()
    	plt.plot(x,y)
	
	
    except KeyboardInterrupt:
        s.close
    

