from sys import stdin

N, M = map(int, stdin.readline().rstrip().split())
A = list(map(int, stdin.readline().rstrip().split()))
B = list(map(int, stdin.readline().rstrip().split()))
merged_array = A + B

print(" ".join(list(map(str, sorted(merged_array)))))