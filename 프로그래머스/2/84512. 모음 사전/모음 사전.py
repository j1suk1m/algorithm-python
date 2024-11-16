from sys import stdin
from itertools import product

def solution(word):
    answer = 0
    vowels = ["A", "E", "I", "O", "U"]
    words = []

    for length in range(1, len(vowels) + 1):
        words.extend(list(map(lambda x: "".join(x), list(product(vowels, repeat=length)))))

    words.sort()

    for idx in range(len(words)):
        if words[idx] == word:
            answer = idx + 1
            break
            
    return answer