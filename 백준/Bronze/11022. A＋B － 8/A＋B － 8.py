from sys import stdin

T = int(stdin.readline().rstrip())

for _ in range(T):
    A, B = map(int, stdin.readline().rstrip().split())
    
    print("Case #{}: {} + {} = {}".format(_ + 1, A, B, A + B))