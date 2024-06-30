while True:
    try:
        first, second, third = map(int, input().split(" "))
        print(max(second - first, third - second) - 1)
    except:
        break