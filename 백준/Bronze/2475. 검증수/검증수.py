from sys import stdin

number_list = list(map(int, stdin.readline().rstrip().split()))
sum_of_squares = 0

for number in number_list:
    sum_of_squares += (number * number)
    
print(sum_of_squares % 10)