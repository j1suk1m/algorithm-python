from sys import stdin

while True:
    number_list = list(map(int, stdin.readline().rstrip().split()))
    number_list.sort()
    maximum = number_list.pop(-1)
    
    if (maximum == 0):
        break
    elif (maximum < sum(number_list) and maximum ** 2 == sum(list(map(lambda x: x ** 2, number_list)))):
        print("right")
    else:
        print("wrong")