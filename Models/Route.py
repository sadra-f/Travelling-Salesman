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

    def copy(self) -> Route:
        res = Route(self.start)
        res.steps = list(self.steps)
        return res

    def visited_all(self, points) -> bool:
        for p in points:
            if not self.visited(p):
                return False
        return True
    
    def visited(self, point) -> bool:
        return point in self.points

    def final(self) -> Point:
        return self.steps[-1]