###b_kh
###ali_coder
import socket
from map_file import run_map_file
start_id,end_id=map(int,input("please enter start_id and end_id:\n").split())

soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
id,port='127.0.0.1',72
soc.connect( (id,port) )
soc.send(bytes ( [start_id,end_id] ) )

file_map = (soc.recv(72000)).decode()
#print(file_map)
best_direction=list( soc.recv(1024) )

#print(best_direction)
run_best_router = run_map_file(best_direction,file_map)
