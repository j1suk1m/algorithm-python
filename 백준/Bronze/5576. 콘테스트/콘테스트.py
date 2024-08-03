from sys import stdin

W = sorted(list(int(stdin.readline().rstrip()) for _ in range(10)), reverse=True)
K = sorted(list(int(stdin.readline().rstrip()) for _ in range(10)), reverse=True)

print(sum(W[:3]), sum(K[:3]))