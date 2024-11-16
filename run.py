from Models.Point import Point
from Algo.TSP import TravelingSalesman
A = Point("A")
B = Point("B")
C = Point("C")
D = Point("D")
E = Point("E")
F = Point("F")

A.add_neighbor(B, 5)
A.add_neighbor(E, 3.5)
A.add_neighbor(D, 5)

B.add_neighbor(A , 5)
B.add_neighbor(E , 4)
B.add_neighbor(C , 5)
B.add_neighbor(F , 5)

C.add_neighbor(B, 5)
C.add_neighbor(E, 4)
C.add_neighbor(D, 5)

D.add_neighbor(A, 5)
D.add_neighbor(E, 3.5)
D.add_neighbor(C, 5)

E.add_neighbor(A, 3.5)
E.add_neighbor(B, 4)
E.add_neighbor(C, 4)
E.add_neighbor(D, 3.5)

F.add_neighbor(B, 5)

pl = [A,B,C,D,E,F]

bfs = TravelingSalesman(pl)
res = bfs.run()
for val in res.keys():
    print(f"{val} : ", end='')
    if res[val] is not None:
        print(f"{res[val]} -> len = {res[val].total_distance()}")
    else:
        print("No Hamiltonian Path Found")