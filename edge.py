###b_kh
###ali_coder

# head and tail is made class Vertex

class Edge:
    def __init__(self,head,tail):
        self.__head=head
        self.__tail=tail

    def get_head(self):
        return self.__head
    def get_tail(self):
        return self.__tail
    def get_weight(self):
        x1,x2=self.__head.get_x(),self.__tail.get_x()
        y1,y2=self.__head.get_y(),self.__tail.get_y()
        weight_edge= (( (x2**2 - x1**2)**(1/2)) + ((y2**2 - y1**2 )**(1/2)))
        return weight_edge