T = int(input())

for test_case in range(1, T + 1):
    numbers = list(map(int, input().split()))
    answer = sum(map(lambda number: number if number % 2 else 0, numbers))
    print("#{} {}".format(test_case, answer))