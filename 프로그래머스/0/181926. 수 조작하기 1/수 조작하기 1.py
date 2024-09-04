def solution(n, control):
    answer = n
    
    for operation in control:
        if operation == "w":
            answer += 1
        elif operation == "s":
            answer -= 1
        elif operation == "d":
            answer += 10
        else:
            answer -= 10
            
    return answer