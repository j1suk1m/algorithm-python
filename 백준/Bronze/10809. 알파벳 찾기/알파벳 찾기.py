from sys import stdin
from string import ascii_lowercase

S = stdin.readline().rstrip()
alphabet_list = list(ascii_lowercase)

for alphabet in alphabet_list:
    print(S.find(alphabet), end=" ")