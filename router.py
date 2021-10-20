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
    #function add_v_e , add vertexes and edges to list self.vertices and dict self.edge
    def add_v_e(self):
        with open(self.map_file_address,'r') as map_file:
            n,e=[int(i) for i in map_file.readline().split()]

            vertices = {}
            #add vertices
            for _ in range(n):
                line=map_file.readline().split()
                ide,x,y=int(line[0]),float(line[1]),float(line[2])
                new_vertex=Vertex(ide,x,y)
                self.__vertices.append(new_vertex)
                vertices[ide]=new_vertex
            # add edges
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
        # copy of self.vertices and dict sefl.edge for calculate under and run heao and (start_id == 0)
        copy_v,copy_e=deepcopy(self.__vertices),deepcopy(self.__edges)
        heap=MinHeap(copy_v)
        heap.modify(start_id,0)

        v_n=dict()
        while end_id in heap:
            # pop shortest vertex of list
            v=heap.pop()
            # calculate size neighbors shortest vertex
            for neighbor in v.get_adjacent_vertice():
                edge = copy_e[v.get_id(),neighbor.get_id()]
                size_v_n = v.get_value() + edge.get_weight()
                # set prev and set value neighbor
                if size_v_n < neighbor.get_value():
                    heap.modify(neighbor.get_id(),size_v_n)
                    neighbor.set_prev(v)
            # add to dict v_n
            v_n[f'{v}'] = v , v.get_adjacent_vertice()

        # found list best_direction
        best_direction , end_v = list() , v_n[str(end_id)][0]

        # add id end_v to list best_direction
        for vertex in self.__vertices:
            if vertex.get_id() is end_id:
                best_direction.append(vertex.get_id())

        # find best route and add vertexes to list best_direction
        while True:
            prev=end_v.get_prev()
            if prev is not None:
                end_v=prev
                best_direction.append(prev.get_id())
            else:
                break

        return best_direction