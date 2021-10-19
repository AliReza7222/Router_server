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
            number_line=int(address_map.readline())
            for _ in range(number_line+1):
                line = address_map.readline().split()
                if len(line) != 0:
                    address_m[int(line[0])] = int(line[1]),int(line[2])

        picture = ig.imread("my_map.jpg")
        print(self.best_direction)
        for number in range(len(self.best_direction)-1):
            x=[address_m[ self.best_direction [ number ] ][0],address_m[ self.best_direction [ number+1 ]][0] ]
            y=[address_m[ self.best_direction [ number ] ][1],address_m[ self.best_direction [ number+1 ]][1] ]
            plt.plot(x,y,marker="o",color="red")

        for id in address_m:
            x,y= address_m[id][0],address_m[id][1]
            plt.scatter(x,y,color="blue",s=25)
            if id == 140 :
                plt.annotate("Home",(x,y),fontsize=9,color="black")
            else:
                plt.annotate(id,(x,y),fontsize=10,color="black")
        if len(self.best_direction) == 1:
            x,y=address_m[self.best_direction[0]][0],address_m[self.best_direction[0]][1]
            plt.scatter(x,y,color="red")
        plt.imshow(picture)
        plt.title('map')
        plt.xlabel("X")
        plt.ylabel("Y")
        #plt.grid()
        plt.show()

