N = list(map(int, list(input())))
is_lucky_straight = sum(N[:len(N)//2]) == sum(N[len(N)//2:])

if is_lucky_straight:
    print("LUCKY")
else:
    print("READY")