import sys

T = int(sys.stdin.readline().rstrip())
times = [300, 60, 10]
result = [0, 0, 0]

if (T % min(times)):
    print("-1")
else:
    idx = 0
    while (T > 0):
        current_button_time = times[idx]
        result[idx] = (T // current_button_time)
        T = T % current_button_time
        idx += 1
    print(" ".join(list(map(str, result))))