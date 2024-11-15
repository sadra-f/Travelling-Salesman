from Models.ND import NeighborDistance as ND

class Point:
    def __init__(self, id):
        self.id = id
        self.neighbors = []
        self.visited = False


    def add_neighbor(self, point, dist):
        self.neighbors.append(ND(self, point, dist))
    

    def neighbors_list(self):
        return [i.neighbor for i in self.neighbors]
    
    def neighbor_dist(self, point):
        for i in self.neighbors:
            if i.neighbor == point:
                return i.distance
        raise ValueError("point is not in neighbors list")

    def neighbor_dist_tuple(self):
        return [(i.neighbor, i.dist) for i in self.neighbors]
    
    def reset_visit(self):
        self.visited = False

    def visit(self):
        self.visited = True

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Point) :
            res += 1 if self.id == value.id else 0
            for i in self.neighbors:
                if i not in value.neighbors:
                    res -= 1
                    break
            return res == 2
        return False


