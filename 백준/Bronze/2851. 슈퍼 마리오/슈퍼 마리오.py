from sys import stdin

scores = list(int(stdin.readline().rstrip()) for _ in range(10))
current = 0
isSolved = False

for score in scores:
    next = current + score
    
    if next >= 100:
        ### 100에 더 가까운 점수 선택
        if next - 100 > 100 - current: 
            print(current)
        else:
            print(next)
        
        isSolved = True
        break
    else:
        current = next

if not isSolved:
    print(current)