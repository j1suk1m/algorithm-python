N = int(input())
height_list = list(map(int, input().split(" ")))
result = 1

for idx in range(len(height_list) - 1):
    if (height_list[idx] <= height_list[idx + 1]):
        result += 1
print(result)