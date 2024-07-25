from sys import stdin

A, B = map(str, stdin.readline().rstrip().split())
A = A[::-1]
B = B[::-1]

for num_of_A, num_of_B in zip(A, B):    
    if num_of_A == num_of_B:
        continue
    elif num_of_A > num_of_B:
        print(A)
        break
    else:
        print(B)
        break