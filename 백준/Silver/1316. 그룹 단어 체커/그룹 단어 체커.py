from sys import stdin

N = int(stdin.readline().rstrip())
count = 0

for _ in range(N):
    isGroupWord = True
    letter_dict = {}
    word = stdin.readline().rstrip()
    
    for i in range(len(word)):
        current_letter = word[i]
        
        if (current_letter in letter_dict.keys() and letter_dict[current_letter] != i - 1):
            isGroupWord = False
            break
        else:
            letter_dict[current_letter] = i
    
    if (isGroupWord):
        count += 1
        
print(count)