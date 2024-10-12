from sys import stdin

input = lambda: stdin.readline().rstrip()

N, M = map(int, input().split())
word_count = dict() ### key: word, value: count

for _ in range(N):
    word = input()
    
    if len(word) < M:
        continue
    elif word in word_count.keys():
        word_count[word] += 1
    else:
        word_count[word] = 1
        
sorted_word = sorted(word_count.keys(), key=lambda word: (-word_count[word], -len(word), word))

for word in sorted_word:
    print(word)