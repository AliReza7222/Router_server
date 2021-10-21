###b_kh
###ali_coder
import matplotlib.pyplot as plt
import matplotlib.image as ig

# found class run_map_file for shows map with use of matplotlib
class run_map_file:
    def __init__(self,best_direction,map_file):
        self.best_direction=best_direction
        self.map_file=map_file
        self.run_mapfile()
    # function run_mapfile for shows route with use of matplotlib
    def run_mapfile(self):
        address_m=dict()
        # read file address_vertex_in_matplotlib.txt that is Coordinates map matplotlib
        with open("address_vertex_in_matplotlib.txt",'r') as address_map:
            number_line=int(address_map.readline())
            for _ in range(number_line+1):
                line = address_map.readline().split()
                if len(line) != 0:
                    address_m[int(line[0])] = int(line[1]),int(line[2])
        # input x if x is "y" draw all routes
        x = input("Do you want show all routes ? (y/n) : ")
        print("ok\nplease waiting for show map.....")
        if x == "y" :
            with open(self.map_file, 'r') as map_ege:
                n_v, n_e = [int(i) for i in map_ege.readline().split()]
                for line in range(n_v + n_e + 1):
                    edge = map_ege.readline().split()
                    if len(edge) == 2:
                        id1, id2 = int(edge[0]), int(edge[1])
                        x = [address_m[id1][0], address_m[id2][0]]
                        y = [address_m[id1][1], address_m[id2][1]]
                        plt.plot(x, y, marker="o", color='#00a4e7', alpha=0.7)
        # show image map in matplotlib
        picture = ig.imread("my_map.jpg")
        # find x , y  of list best_direction for draw line best route
        for number in range(len(self.best_direction)-1):
            x=[address_m[ self.best_direction [ number ] ][0],address_m[ self.best_direction [ number+1 ]][0] ]
            y=[address_m[ self.best_direction [ number ] ][1],address_m[ self.best_direction [ number+1 ]][1] ]
            plt.plot(x,y,marker="o",color="#04b04d")
        # draw dot for all vertexes in map and write id vertex
        for id in address_m:
            x,y= address_m[id][0],address_m[id][1]
            plt.scatter(x,y,color="#fa00d6",s=20,alpha=0.5)
            if id == 140 :
                plt.annotate("Home",(x,y),fontsize=9,color="black")
            else:
                plt.annotate(id,(x,y),fontsize=7,color="black")

        if len(self.best_direction) == 1:
            x,y=address_m[self.best_direction[0]][0],address_m[self.best_direction[0]][1]
            plt.scatter(x,y,color="#04b04d")

        # show map
        plt.imshow(picture)
        plt.title('Map')
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.show()
        print("Good luck.")

