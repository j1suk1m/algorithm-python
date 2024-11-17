from sys import stdin

input = lambda: stdin.readline().rstrip()

def back_tracking(number_idx, current_value):
    global max_value, min_value
    global add, sub, mul, div

    if number_idx == N:
        max_value = max(max_value, current_value)
        min_value = min(min_value, current_value)
        return

    if add > 0:
        add -= 1
        back_tracking(number_idx + 1, current_value + A[number_idx])
        add += 1
    if sub > 0:
        sub -= 1
        back_tracking(number_idx + 1, current_value - A[number_idx])
        sub += 1
    if mul > 0:
        mul -= 1
        back_tracking(number_idx + 1, current_value * A[number_idx])
        mul += 1
    if div > 0:
        div -= 1

        if current_value < 0:
            back_tracking(number_idx + 1, -((-current_value) // A[number_idx]))
        else:
            back_tracking(number_idx + 1, current_value // A[number_idx])
        
        div += 1

N = int(input())
A = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_value = -int(1e9)
min_value = int(1e9)

back_tracking(1, A[0])

print(max_value)
print(min_value)