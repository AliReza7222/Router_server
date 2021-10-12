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
        with open(self.map_file_address,'r') as map_file:
            n,e=[int(i) for i in map_file.readline().split()]

            vertices = {}
            for _ in range(n):
                line=map_file.readline().split()
                ide,x,y=int(line[0]),float(line[1]),float(line[2])
                new_vertex=Vertex(ide,x,y)
                self.__vertices.append(new_vertex)
                vertices[ide]=new_vertex

            for _ in range(e):
                line=map_file.readline().split()
                id1,id2 = int(line[0]),int(line[1])
                head,tail = vertices[id1],vertices[id2]
                new_edge = Edge(head,tail)
                self.__edges[id1,id2] = new_edge
                self.__edges[id2,id1] = new_edge
                head.append_adjacent_vertice(tail)
                tail.append_adjacent_vertice(head)

    def find_shortest_path(self,start_id,end_id):
        copy_v,copy_e=deepcopy(self.__vertices),deepcopy(self.__edges)
        heap=MinHeap(copy_v)
        heap.modify(start_id,0)
        while end_id in heap:
            v=heap.pop()
            for neighbor in v.get_adjacent_vertice():
                edge=copy_e[v.get_id(),neighbor.get_id()]
                size_v_n = v.get_value() + edge.get_weight()
                if size_v_n < neighbor.get_value():
                    heap.modify(neighbor.get_id(),size_v_n)
                    neighbor.set_prev(v)
r=Router('maps.txt')
print(r.find_shortest_path(60,72))