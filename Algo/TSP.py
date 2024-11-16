from Models.Point import Point
from Models.Route import Route

class TravelingSalesman:
    def __init__(self, points):
        self.points = points
        self.routes = {p : [] for p in self.points}
        self.best_routes = {p : Route(p) for p in self.points}

    def run(self):
        pass


    def bfs(self, start:Point):
        #use BFS instead of DFS (use queue) make a new route for each neighbor newly visited keep the visited nodes in the route
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



