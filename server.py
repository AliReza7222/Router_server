###b_kh
###ali_coder

import socket,threading
from router import Router

def Tread(client):
        router=Router('maps.txt')
        start,end=tuple(client.recv(1024))
        best_direction = router.find_shortest_path( start,end )

        with open("maps.txt",'r') as file_map:
            map = file_map.read()
            client.send(map.encode())

        client.send(bytes(best_direction))
        client.close()

id,port="127.0.0.1",72
soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.bind((id,port))
soc.listen(10)

for _ in range(1,11):
    client,address=soc.accept()
    threading.Thread(target=Tread,args=(client,)).start()
    print(f"Hi client {_}")
soc.close()
