from sys import stdin

input = lambda: stdin.readline().rstrip()

def back_tracking():
    global count
    
    if len(selected_card_indices) == K:
        number = "".join(list(map(lambda index: str(cards[index]), selected_card_indices)))
        
        if number not in answer:
            count += 1
            answer.append(number)
            
        return
    
    for index in range(N):
        if index not in selected_card_indices:
            selected_card_indices.append(index)
            back_tracking()
            selected_card_indices.pop()
    
N = int(input())
K = int(input())
cards = list(int(input()) for _ in range(N))
selected_card_indices = []
answer = []
count = 0

back_tracking()

print(count)