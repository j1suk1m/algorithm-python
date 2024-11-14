from sys import stdin

input = lambda: stdin.readline().rstrip()

def get_fastest_time(stick_length: int, position: int) -> int:
    return min(stick_length - position, position)

def get_slowest_time(stick_length: int, position: int) -> int:
    return max(stick_length - position, position)

T = int(input())

for _ in range(T):
    stick_length, N = map(int, input().split())
    positions = list(int(input()) for _ in range(N))

    fastest_times = list(map(lambda position: get_fastest_time(stick_length, position), positions))
    slowest_times = list(map(lambda position: get_slowest_time(stick_length, position), positions))

    print(max(fastest_times), max(slowest_times))