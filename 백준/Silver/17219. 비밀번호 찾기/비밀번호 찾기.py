from sys import stdin

N, M = map(int, stdin.readline().rstrip().split())
password_dict = dict()

for _ in range(N):
    site, password = map(str, stdin.readline().rstrip().split())
    password_dict[site] = password
    
for _ in range(M):
    site = stdin.readline().rstrip()
    print(password_dict[site])