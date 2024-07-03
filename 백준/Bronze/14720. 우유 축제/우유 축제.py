from sys import stdin

N = int(stdin.readline().rstrip())
milk_stores =stdin.readline().rstrip().replace(" ", "")
milk = ['0', '1', '2']
result = 0
milk_idx = 0
idx = 0
milk_len = len(milk)

while True:
    idx = milk_stores.find(milk[milk_idx], idx)
    
    if (idx == -1):
        break
    else:
        result += 1
        milk_idx = (milk_idx + 1) % milk_len
        
print(result)