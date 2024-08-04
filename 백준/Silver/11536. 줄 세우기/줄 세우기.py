from sys import stdin

N = int(stdin.readline().rstrip())
names = list(stdin.readline().rstrip() for _ in range(N))
increasing_names = sorted(names)

if names == increasing_names: ### 오름차순
    print("INCREASING")
elif names == increasing_names[::-1]: ### 내림차순
    print("DECREASING")
else: ### 그 외 
    print("NEITHER")