from sys import stdin

id = stdin.readline().rstrip()

for i in range(3):
    for j in range(3):
        if (i != 1 or j != 1):
            print(":fan:", end="")
        else:
            print(":" + id + ":", end="")
            
    print()