from sys import stdin

container_num_list = list(map(int, stdin.readline().rstrip().split()))
refunded_amount = sum([x * 5 for x in container_num_list])

print(refunded_amount)