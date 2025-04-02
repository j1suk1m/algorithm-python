from sys import stdin

input = lambda: stdin.readline().rstrip()
minimum = 0
maximum = 11

while True:
    number = int(input())
    
    if number == 0:
        break
    else:
        response = input()
        
        if response == "too high":
            maximum = min(maximum, number);
        elif response == "too low":
            minimum = max(minimum, number);
        elif minimum < number and number < maximum:
            print("Stan may be honest")
            minimum = 0
            maximum = 11
        else:
            print("Stan is dishonest")
            minimum = 0
            maximum = 11