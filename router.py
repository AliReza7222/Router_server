from Vertex import Vertex
from edge import Edge
from heap import MinHeap
from copy import deepcopy


# map_file_address equel address file text map in project karyar in the from of string
class Router:
    def __init__(self, map_file_address):
        self.map_file_address = map_file_address
        self.__edges = {}
        self.__vertices = []
        self.add_vertex_edge()

    # function add_vertex_edge , add vertexes and edges to list self.vertices and dict self.edge
    def add_vertex_edge(self):
        with open(self.map_file_address, 'r') as map_file:
            n_vertex, n_edge = [int(i) for i in map_file.readline().split()]

            vertices = {}
            # add vertices
            for _ in range(n_vertex):
                line = map_file.readline().split()
                ide, x, y = int(line[0]), float(line[1]), float(line[2])
                new_vertex = Vertex(ide, x, y)
                self.__vertices.append(new_vertex)
                vertices[ide] = new_vertex
            # add edges
            for _ in range(n_edge):
                line = map_file.readline().split()
                id1, id2 = int(line[0]), int(line[1])
                head, tail = vertices[id1], vertices[id2]
                new_edge = Edge(head, tail)
                self.__edges[id1, id2] = new_edge
                self.__edges[id2, id1] = new_edge
                head.append_adjacent_vertice(tail)
                tail.append_adjacent_vertice(head)

    def find_shortest_path(self, start_id, end_id):
        # copy of self.vertices and dict self.edge for calculate under and run heap and (start_id == 0)
        copy_list_vertex, copy_dict_edge = deepcopy(self.__vertices), deepcopy(self.__edges)
        heap = MinHeap(copy_list_vertex)
        heap.modify(start_id, 0)
        dict_vertex = dict()

        while end_id in heap:

            # pop shortest vertex of list
            small_vertex = heap.pop()

            # calculate size neighbors shortest vertex
            for neighbor in small_vertex.get_adjacent_vertice():
                edge = copy_dict_edge[small_vertex.get_id(), neighbor.get_id()]
                size_vertex_neighbor = small_vertex.get_value() + edge.get_weight()

                # set prev and set value neighbor
                if size_vertex_neighbor < neighbor.get_value():
                    heap.modify(neighbor.get_id(), size_vertex_neighbor)
                    neighbor.set_prev(small_vertex)

            # add to dict_vertex
            dict_vertex[f'{small_vertex}'] = small_vertex, small_vertex.get_adjacent_vertice()

        # found list best_direction
        best_direction, end_vertex = list(), dict_vertex[str(end_id)][0]

        # add id end_v to list best_direction
        for vertex in self.__vertices:
            if vertex.get_id() is end_id:
                best_direction.append(vertex.get_id())

        # find best route and add vertexes to list best_direction
        while True:
            prev = end_vertex.get_prev()
            if prev is not None:
                end_vertex = prev
                best_direction.append(prev.get_id())
            else:
                break

        return best_direction
