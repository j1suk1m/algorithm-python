from sys import stdin

x = int(stdin.readline().rstrip())
y = int(stdin.readline().rstrip())

if (x < 0):
    if (y > 0):
        print("2")
    else:
        print("3")
else:
    if (y > 0):
        print("1")
    else:
        print("4")

