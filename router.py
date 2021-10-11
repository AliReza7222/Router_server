###b_kh
###ali_coder
from Vertex import Vertex
from edge import Edge
from heap import MinHeap
from copy import deepcopy

# map_file_address equel address file text map in project karyar in the from of string
class Router:
    def __init__(self,map_file_address):
        self.map_file_address=map_file_address
        self.__edges={}
        self.__vertices=[]
        self.add_v_e()
    def add_v_e(self):
        with open(self.map_file_address,'r') as v_e:

            number_v_e = v_e.readline(3)

            n_v,n_e= int(number_v_e[0]),int(number_v_e[2])

            list_v=[v_e.readline().strip('\n').split(' ') for v in range(n_v+1)]
            list_v.remove([''])
            list_e=[v_e.readline().strip('\n').split(' ') for e in range(n_e)]

        for vertex in list_v:
            self.__vertices.append(Vertex(int(vertex[0]),float(vertex[1]),float(vertex[2])))

        head,trail=0,0
        for edge in list_e:
            v_head,v_trail=edge[0],edge[1]
            for vertex in list_v:
                if v_head in vertex:
                    head=Vertex(int(v_head),float(vertex[1]),float(vertex[2]))
                if v_trail in vertex:
                    trail=Vertex(int(v_trail),float(vertex[1]),float(vertex[2]))

            self.__edges[int(v_head),int(v_trail)] = Edge(head,trail)
            self.__edges[int(v_trail),int(v_head)]=  Edge(trail,head)

    def find_shortest_path(self,start_id,end_id):
        copy_v=deepcopy(self.__vertices)
        copy_e=deepcopy(self.__edges)
        heap=MinHeap(copy_v)
        heap.modify(start_id,0)
        while end_id in heap:
             v=heap.pop()
             for id,edge in zip(copy_e.keys(),copy_e.values()):
                if v.get_id() is id[0]:
                    size_n_v= v.get_value() + edge.get_weight()
                    neighboor=edge.get_tail()
                    size_neighboor=neighboor.get_value()
                    print('size v + road = ',size_n_v,'\tvalue neighboor is :',size_neighboor)

r=Router('maps.txt')
print(r.find_shortest_path(60,72))