N = int(input())
target_list = list(map(int, input().split(" ")))
current_list = list(map(int, input().split(" ")))
result = 0

for (current, target) in zip(current_list, target_list):
    if (current > target):
        result += (current - target)
print(result)