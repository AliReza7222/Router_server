###b_kh
###ali_coder

import socket,pickle

soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
start_id,end_id=map(int,input().split())
id,port='127.0.0.1',72
soc.connect( (id,port) )
soc.send(bytes ( [start_id,end_id] ) )
file_map = (soc.recv(1024)).decode()
best_direction=pickle.loads(soc.recv(1024))
