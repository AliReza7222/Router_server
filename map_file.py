###b_kh
###ali_coder
import matplotlib.pyplot as plt
import matplotlib.image as ig

class run_map_file:
    def __init__(self,best_direction,map_file):
        self.best_direction=best_direction
        self.map_file=map_file
        self.run_mapfile()

    def run_mapfile(self):
        address_m=dict()
        with open("address_vertex_in_matplotlib.txt",'r') as address_map:
            number_line=int(address_map.readline(1))
            for _ in range(number_line+1):
                line = address_map.readline().split()
                if len(line) != 0:
                    address_m[int(line[0])] = int(line[1]),int(line[2])

        picture = ig.imread("2021-10-03_082304.jpg")
        x,y=[address_m[60][0],address_m[61][0]],[address_m[60][1],address_m[61][1]]
        x2,y2=[address_m[61][0],address_m[64][0]],[address_m[61][1],address_m[64][1]]

        id_best=[vertex.get_id() for vertex in self.best_direction]
        print(id_best)
        for number in range(len(id_best)-1):
            x=[address_m[ id_best [ number ] ][0],address_m[ id_best [ number+1 ]][0] ]
            y=[address_m[ id_best [ number ] ][1],address_m[ id_best [ number+1 ]][1] ]
            plt.plot(x,y,marker="o",color="red")
        # plt.plot(x,y,marker="o",color="red")
        # plt.plot(x2,y2,marker="o",color="red")
        # plt.annotate(60,(x[0],y[0]),fontsize=18,color="blue")
        for id in address_m:
            x,y= address_m[id][0],address_m[id][1]
            plt.scatter(x,y,color="blue",s=50)
        if len(id_best) == 1:
            x,y=address_m[id_best[0]][0],address_m[id_best[0]][1]
            plt.scatter(x,y,color="red")
        plt.imshow(picture)
        plt.title('**best route**')
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.show()

