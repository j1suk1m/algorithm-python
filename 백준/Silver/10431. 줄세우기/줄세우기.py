from sys import stdin

input = lambda: stdin.readline().rstrip()

P = int(input())

for _ in range(P):
    test_case = list(map(int, input().split()))
    T = test_case[0]
    heights = test_case[1:]
    number_of_steps = 0
    N = 20
    
    for current in range(1, N):
        for rest in range(current):
            if heights[rest] > heights[current]:
                number_of_steps += 1
                
    print(T, number_of_steps)