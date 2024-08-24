from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())
employee_dict = dict()

for _ in range(N):
    name, log = map(str, input().split())
    
    if name in employee_dict.keys():
        del employee_dict[name]
    else:
        employee_dict[name] = 0
        
employee_dict = sorted(employee_dict.items(), reverse=True)

for name, value in employee_dict:
    print(name)