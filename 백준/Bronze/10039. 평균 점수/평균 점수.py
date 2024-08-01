from sys import stdin

sum = 0

for _ in range(5):
    score = int(stdin.readline().rstrip())
    
    if score >= 40:
        sum += score 
    else:
        sum += 40
        
print(sum // 5)