# b_kh
# ali_coder
import matplotlib.pyplot as plt
import matplotlib.image as ig


# found class run_map_file for shows map with use of matplotlib
class run_map_file:
    def __init__(self, best_direction, map_file):
        self.best_direction = best_direction
        self.map_file = map_file
        self.run_mapfile()

    # reads file address_vertex_in_matplotlib.txt for use in map
    def read_map(self):
        address_m = dict()
        # read file address_vertex_in_matplotlib.txt that is Coordinates map matplotlib
        with open("address_vertex_in_matplotlib.txt", 'r') as address_map:
            number_line = int(address_map.readline())
            for _ in range(number_line + 1):
                line = address_map.readline().split()
                if len(line) != 0:
                    address_m[int(line[0])] = int(line[1]), int(line[2])
        return address_m

    # this func is for draw best_route in map
    def draw_best_rout(self, address_m):
        # find x , y  of list best_direction for draw line best route
        for number in range(len(self.best_direction) - 1):
            x = [address_m[self.best_direction[number]][0], address_m[self.best_direction[number + 1]][0]]
            y = [address_m[self.best_direction[number]][1], address_m[self.best_direction[number + 1]][1]]
            plt.plot(x, y, marker="o", color="#006111")

        # if start_id equal end_id
        if len(self.best_direction) == 1:
            x, y = address_m[self.best_direction[0]][0], address_m[self.best_direction[0]][1]
            plt.scatter(x, y, color="#04b04d")

    # this func is for draw all route or don't draw all route
    def run_condition(self, address_m, yes=None, no=None):
        # if yes equal 'y' , draw all route in map
        if yes == 'y':
            # reads file maps.txt for draw all route in map
            with open(self.map_file, 'r') as map_ege:
                n_v, n_e = [int(i) for i in map_ege.readline().split()]
                for line in range(n_v + n_e + 1):
                    edge = map_ege.readline().split()
                    if len(edge) == 2:
                        id1, id2 = int(edge[0]), int(edge[1])
                        x = [address_m[id1][0], address_m[id2][0]]
                        y = [address_m[id1][1], address_m[id2][1]]
                        plt.plot(x, y, marker="o", color='#00a4e7', alpha=0.7)
                # write id for any place
                for id in address_m:
                    x, y = address_m[id][0], address_m[id][1]
                    plt.annotate(id, (x, y), fontsize=7, color="black")
        # if no equal 'n' only draw dot for any id and write name id
        if no == 'n':
            for id in address_m:
                x, y = address_m[id][0], address_m[id][1]
                plt.annotate(id, (x, y), fontsize=7, color="black")
                plt.scatter(x, y, color="#fa00d6", s=20, alpha=0.5)


    # function run_mapfile for shows route with use of matplotlib
    def run_mapfile(self):
        address_m = self.read_map()

        # input for show all route or show only best route and write id vertex
        x = input("Do you want show all routes ? (y/n) : ")

        # input x if x is "y" draw all routes
        if x == "y":
            self.run_condition(address_m, yes="y")
            print("ok\nplease waiting for show map.....\n")

        # if x is "n" draw dot for all vertexes in map and write id vertex
        elif x == "n":
            self.run_condition(address_m, no="n")
            print("ok\nplease waiting for show map.....")

        # else if no "n" and no "y" raise Error
        else:
            raise Exception("Error entryway")

        # show image map in matplotlib
        picture = ig.imread("my_map.jpg")

        # draw best_route in map
        self.draw_best_rout(address_m)

        # show map
        plt.imshow(picture)
        plt.title(' ( in map best route is shown with color green ) ')
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.show()
