from Models.Point import Point
from Models.Route import Route

class TravelingSalesman:
    def __init__(self, points):
        self.points = points
        self.routes = {p : None for p in self.points}
        self.best_route = {p : None for p in self.points}

    def run(self):
        for p in self.points:
            routes = self.bfs(p)
            if len(routes) > 0:
                self.routes[p] = routes
                best = routes[0].total_distance()
                self.best_route[p] = routes[0]
                for r in routes:
                    if r.total_distance() < best:
                        best = r.total_distance()
                        self.best_route[p] = r
        return self.best_route



    def bfs(self, start:Point):
        routes = []
        queue = [Route(start)]

        while len(queue) > 0:
            current_r = queue.pop(0)
            if current_r.visited_all(self.points):
                routes.append(current_r)
                continue
            for p in current_r.final().neighbors:
                if not current_r.visited(p):
                    tmp_r = current_r.copy()
                    tmp_r.add_point(p)
                    queue.append(tmp_r)
        
        return routes



