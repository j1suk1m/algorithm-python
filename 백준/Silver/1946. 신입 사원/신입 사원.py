from sys import stdin

input = lambda: stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    N = int(input())
    ranks = list(tuple(list(map(int, input().split()))) for _ in range(N))
    ranks_sorted_by_document = sorted(ranks, key=lambda x: x[0])
    highest_rank_of_interview = ranks_sorted_by_document[0][1]
    answer = 1
    
    for employee in range(1, N):
        interview_rank = ranks_sorted_by_document[employee][1]
        
        if interview_rank < highest_rank_of_interview:
            highest_rank_of_interview = interview_rank
            answer += 1 
            
    print(answer)