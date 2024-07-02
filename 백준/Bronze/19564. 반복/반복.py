from sys import stdin

S = stdin.readline().rstrip()
result = 1
ascii = ord(S[0])

for idx in range(1, len(S)):
    current_ascii = ord(S[idx])
    
    if (ascii >= current_ascii):
        result += 1
        
    ascii = current_ascii
    
print(result)