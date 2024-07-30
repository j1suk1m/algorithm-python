from sys import stdin

n = int(stdin.readline().rstrip()) 
target_sequence = [int(stdin.readline().rstrip()) for _ in range(n)]
stack = []
answer = []
current_number = 1

try:
    for target_number in target_sequence:
        if target_number in stack: ### 수열의 숫자가 스택에 있는 경우
            while True:
                if stack.pop() == target_number: ### 해당 숫자가 나올 때까지 pop
                    answer.append('-')
                    break
        else: ### 수열의 숫자가 아직 스택에 들어가지 않은 경우
            while current_number <= target_number: ### 마지막으로 push된 숫자의 다음 수부터 해당 숫자까지 push
                stack.append(current_number)
                answer.append('+')
                current_number += 1

            stack.pop()
            answer.append('-')
except: 
    print("NO")
else:
    print("\n".join(answer))