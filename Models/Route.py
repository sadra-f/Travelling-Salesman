from Models.PD import PointDistance as PD
from Models.Point import Point
class Route:
    def __init__(self, start):
        self.start = start
        self.steps = []
        self.points = [start]

    def add_point(self, point:Point):
        if point not in self.points[-1].neighbors:
            raise ValueError("new point is not a neighbors of the last point")
        self.steps.append(PD(self.start, point, self.points[-1].neighbor_dist(point)))
        self.points.append(point)

    def copy(self):
        res = Route(self.start)
        res.steps = list(self.steps)
        return res

    def visited_all(self, points):
        for p in points:
            if p not in self.points:
                return False
        return True
    
    def final(self):
        return self.steps[-1]