from sys import stdin

input = lambda: stdin.readline().rstrip()

N = sorted(list(map(int, list(input()))), reverse=True)

if sum(N) % 3 != 0 or N[-1] != 0:
    print(-1)
else:
    print("".join(list(map(str, N))))