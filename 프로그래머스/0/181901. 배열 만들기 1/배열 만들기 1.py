def solution(n, k):
    answer = []
    
    for number in range(1, n + 1):
        if number % k == 0:
            answer.append(number)
            
    return answer