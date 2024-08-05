from sys import stdin
from heapq import heappush, heappop

N = int(stdin.readline().rstrip())
heap = []
answer = 0

for _ in range(N):
    heappush(heap, int(stdin.readline().rstrip()))

while len(heap) >= 2:
    ### 가장 작은 수 두 개를 뺀 뒤 합해서 다시 힙큐에 넣기
    number1 = heappop(heap)
    number2 = heappop(heap)
    answer += (number1 + number2)
    heappush(heap, number1 + number2)
    
print(answer)