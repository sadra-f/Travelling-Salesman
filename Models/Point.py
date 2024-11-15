from Models.ND import NeighborDistance as PD

class Point:
    def __init__(self, id):
        self.id = id
        self.neighbors = []
        self.visited = False


    def add_neighbor(self, point, dist):
        self.neighbors.append(PD(self, point, dist))
    

    def neighbors_list(self):
        return [i.neighbor for i in self.neighbors]
    

    def neighbor_dist_tuple(self):
        return [(i.neighbor, i.dist) for i in self.neighbors]
    
    def reset_visit(self):
        self.visited = False

    def visit(self):
        self.visited = True