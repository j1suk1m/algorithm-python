from sys import stdin

N = int(stdin.readline().rstrip())
word_list = []

for _ in range(N):
    word_list.append(stdin.readline().rstrip())
    
word_list = list(set(word_list))
word_list = sorted(word_list, key=lambda x: (len(x), x))

for word in word_list:
    print(word)