from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())
book_dict = dict()

for _ in range(N):
    book = input()
    
    if book in book_dict.keys():
        book_dict[book] += 1
    else:
        book_dict[book] = 1

book_list = sorted(book_dict.items(), key=lambda x: (-x[1], x[0]))
print(book_list[0][0])