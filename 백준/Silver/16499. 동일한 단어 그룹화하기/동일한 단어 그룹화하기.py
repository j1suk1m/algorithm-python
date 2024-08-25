from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())
words = set()

for _ in range(N):
    word = sorted(list(input()))
    words.add("".join(word))
    
print(len(words))