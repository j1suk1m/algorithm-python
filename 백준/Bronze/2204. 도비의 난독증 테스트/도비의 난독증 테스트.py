from sys import stdin

while True:
    n = int(stdin.readline().rstrip())
    
    if n == 0:
        break
    
    words = [stdin.readline().rstrip() for _ in range(n)]
    words = sorted(words, key=lambda word: word.lower())
    
    print(words[0])