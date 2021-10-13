###b_kh
###ali_coder
class Vertex:
    def __init__(self, identity , x , y , value=float('inf')):
        self.__identity=identity
        self.__x=x
        self.__y=y
        self.__adjacent_vertice=[]
        self.__value=value
        self.__prev=None


    def get_id(self):
        return self.__identity
    def set_id(self,id):
        self.__identity=id

    def get_y(self):
        return self.__y
    def set_y(self,y):
        self.__y=y

    def get_x(self):
        return self.__x
    def set_x(self,x):
        self.__x=x

    def get_value(self):
        return self.__value
    def set_value(self,value):
        self.__value=value

    def get_adjacent_vertice(self):
        return self.__adjacent_vertice
    def append_adjacent_vertice(self,neighbor):
        self.__adjacent_vertice.append(neighbor)

    def get_prev(self):
        return self.__prev
    def set_prev(self,prev):
        self.__prev=prev


    def __eq__(self, other):
            return other.__identity == self.__identity

    def __gt__(self, other):
        if not isinstance(other,Vertex):
            raise TypeError(str(other) + 'is not and instance of '+ self.__class__.__name__)
        return self.__value < other.__value

    def __lt__(self, other):
        if not isinstance(other,Vertex):
            raise TypeError(str(other) + 'is not and instance of '+ self.__class__.__name__)
        return other.__value > self.__value

    def __ge__(self, other):
        if not isinstance(other,Vertex):
            raise TypeError(str(other) + 'is not and instance of ' + self.__class__.__name__)
        return self.__value <= other.__value

    def __le__(self, other):
        if not isinstance(other,Vertex):
            raise TypeError(str(other) + 'is not and instance of ' + self.__class__.__name__)
        return other.__value >= self.__value

    def __str__(self):
        return str(self.__identity)