from sys import stdin

N = int(stdin.readline().rstrip())
numbers = list(map(int, stdin.readline().rstrip().split()))
numbers = sorted(set(numbers)) ### 중복 제거 후 오름차순 정렬

print(" ".join(list(map(str, numbers))))
