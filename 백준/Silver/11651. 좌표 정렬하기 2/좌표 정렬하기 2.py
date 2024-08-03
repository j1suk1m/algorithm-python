from sys import stdin

N = int(stdin.readline().rstrip())
coordinates = list(tuple(map(int, stdin.readline().rstrip().split())) for _ in range(N))
coordinates = sorted(coordinates, key=lambda coordinate: (coordinate[1], coordinate[0]))

for coordinate in coordinates:
    print(coordinate[0], coordinate[1])