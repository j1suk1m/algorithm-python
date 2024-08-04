from sys import stdin

K = int(stdin.readline().rstrip())

for order in range(1, K + 1):
    input = list(map(int, stdin.readline().rstrip().split()))
    N = input[0]
    scores = sorted(input[1:], reverse=True)
    largest_gap = max(list(scores[x] - scores[x + 1] for x in range(N - 1)))
    
    print("Class {}".format(order))
    print("Max {}, Min {}, Largest gap {}".format(scores[0], scores[N - 1], largest_gap))