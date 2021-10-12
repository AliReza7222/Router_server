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

        head, trail = None, None
        for edge in list_e:
            v_head, v_trail = edge[0], edge[1]
            for vertex in list_v:
                if v_head in vertex:
                    head = Vertex(int(v_head), float(vertex[1]), float(vertex[2]))
                if v_trail in vertex:
                    trail = Vertex(int(v_trail), float(vertex[1]), float(vertex[2]))

            self.__edges[int(v_head), int(v_trail)] = Edge(head, trail)
            self.__edges[int(v_trail), int(v_head)] = Edge(trail, head)
        for v in self.__vertices:
            for e_k,e_v in zip(self.__edges.keys(),self.__edges.values()):
                if v.get_id() is e_k[0]:
                    v.append_adjacent_vertice(e_v.get_tail())

    def find_shortest_path(self,start_id,end_id):
        copy_v=deepcopy(self.__vertices)
        copy_e=deepcopy(self.__edges)
        heap=MinHeap(copy_v)
        heap.modify(start_id,0)
        while end_id in heap:
            v=heap.pop()
            for neighbor in v.get_adjacent_vertice():
                edge=Edge(v,neighbor)
                size_v_n=v.get_value()+edge.get_weight()
                print(size_v_n,neighbor.get_value())
                ## --> bog : value is inf
                #if size_v_n > neighbor.get_value():
                    #heap.modify(neighbor,size_v_n)
                    #neighbor.set_prev(v)
r=Router('maps.txt')
print(r.find_shortest_path(72,60))