from Models.ND import NeighborDistance as ND

class Point:
    id = 0
    def __init__(self, str_rep=None):
        self.str_rep = str_rep
        self._id = Point.id
        Point.id += 1
        self.neighbors_distances = []
        self.neighbors = []


    def add_neighbor(self, point, dist):
        self.neighbors_distances.append(ND(self, point, dist))
        self.neighbors.append(point)
    
    
    def neighbor_dist(self, point):
        for i in self.neighbors_distances:
            if i.neighbor == point:
                return i.dist
        raise ValueError("point is not in neighbors list")

    def neighbor_dist_tuple(self):
        return [(i.neighbor, i.dist) for i in self.neighbors_distances]

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Point) :
            res = 0
            res = 1 if self._id == value._id else 0
            for i in self.neighbors_distances:
                if i not in value.neighbors_distances:
                    res -= 1
                    break
            return res == 1
        return False


    def __str__(self) -> str:
        return self.str_rep
    

    def __repr__(self) -> str:
        return self.__str__()
    
    def __hash__(self) -> int:
        return self._id