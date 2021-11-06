# b_kh
# ali_coder

import socket
import threading
import json
import winsound
import time
from router import Router


# found thread for process
def tread(client, name):
        router = Router('maps.txt')
        start, end = tuple(json.loads(client.recv(1024)))
        best_direction = router.find_shortest_path(start, end)
        client.send(name.encode())
        client.send("maps.txt".encode())
        client.send(f'{best_direction}'.encode())
        client.close()

# play sound for active and disable server
def load_sound(address):
    winsound.PlaySound(address, winsound.SND_FILENAME)


# found socket for server with id and port appoint
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
id, port = "127.0.0.1", 72
soc.bind((id, port))
soc.listen(10)
print("started server\nwaiting for connect clients......")


load_sound("sound/active.wav")
# listen to ten client for give answer
for number in range(1, 11):
    client, address = soc.accept()
    name = f'client {number}'
    threading.Thread(target=tread, args=(client, name)).start()
    print(f"\nconnection {name} to server .")

print("\nThe server was disabled")
soc.close()
time.sleep(5)
load_sound('sound/end.wav')
