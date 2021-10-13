###b_kh
###ali_coder
import socket,threading
from router import Router
def Tread(client):
        router=Router('maps.txt')
        start,end=(client.recv(1024)).decode()
        best_direction=router.find_shortest_path( start,end )
        client.send(bytes(best_direction))
        client.close()

id,port="",72
soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.bind((id,port))
soc.listen(10)
for _ in range(10):
    client,address=soc.accept()
    threading.Thread(target=Tread,args=(client,))
soc.close()