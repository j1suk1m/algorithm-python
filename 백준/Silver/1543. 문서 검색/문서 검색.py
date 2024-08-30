from sys import stdin

input = lambda: stdin.readline().rstrip()

document = input()
word = input()
document_length = len(document)
word_length = len(word)
left = 0
right = word_length - 1
answer = 0

while right < document_length:
    if document[left:right + 1] == word:
        answer += 1
        left = right + 1
        right += word_length
    else:
        left += 1
        right += 1
        
print(answer)