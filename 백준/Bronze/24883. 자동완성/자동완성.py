from sys import stdin

alphabet = stdin.readline().rstrip()

if (alphabet == 'n' or alphabet == 'N'):
    print("Naver D2")
else:
    print("Naver Whale")