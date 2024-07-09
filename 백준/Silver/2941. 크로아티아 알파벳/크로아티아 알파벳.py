from sys import stdin

word = stdin.readline().rstrip()
word_len = len(word)
croatia_alphabets = ["c=", "c-", "d-", "lj", "nj", "s=", "z="]
count = 0
i = 0

while (i < word_len):    
    if (i < word_len - 1 and word[i: i + 2] in croatia_alphabets):
        i += 2
    elif (i < word_len - 2 and word[i: i + 3] == "dz="):
        i += 3
    else:
        i += 1
    count += 1
    
print(count)