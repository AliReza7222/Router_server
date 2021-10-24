###b_kh
###ali_coder
import socket , json
from map_file import run_map_file
def Run_client():
    #input start_id and end_id for show shortest route
    start_id,end_id=map(int,input("please enter start_id and end_id:\n").split())

    #found socket for connect to server and send to server start_id and end_id
    soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    id ,port = '127.0.0.1' ,72
    soc.connect( (id,port) )
    soc.send( f'{[start_id,end_id]}'.encode() )

    #recive file_map and best_direction of server
    name_client = (soc.recv(100)).decode()
    file_map = (soc.recv(1024)).decode()
    best_direction=json.loads(( soc.recv(1024) ).decode())

    #enteries to class run_map_file for run project
    run_best_router = run_map_file(best_direction,file_map)
    return name_client
# loop for number run project
for number in range(1,11):
    name = Run_client()
    if name == 'client 10' :
        print("\nThe connection to the server was lost.")
        break
    # enter for continue or end
    enter = input("Do you want continue ? (y/n): ")
    if enter == "y" :
        continue
    elif enter == "n" :
        print("you came out of program.\nGood luck.")
        break
    else:
        raise Exception("Error entryway")
