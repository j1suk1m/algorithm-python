from sys import stdin

X = list(map(int, list(stdin.readline().rstrip())))
result = 0

while (len(X) > 1):
    X = list(map(int, list(str(sum(X)))))
    result += 1
    
print(result)
print("NO") if X[0] % 3 else print("YES")