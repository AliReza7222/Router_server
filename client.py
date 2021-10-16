###b_kh
###ali_coder

import socket,pickle
from map_file import run_map_file

soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
start_id,end_id=map(int,input("please enter your router:\n").split())
id,port='127.0.0.1',72
soc.connect( (id,port) )
soc.send(bytes ( [start_id,end_id] ) )
file_map = (soc.recv(1024)).decode()
best_direction=pickle.loads(soc.recv(1024))
run_best_router = run_map_file(best_direction,file_map)
