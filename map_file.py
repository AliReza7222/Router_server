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
        plt.plot(x,y,marker="o",color="blue",)
        plt.imshow(picture)
        plt.show()

