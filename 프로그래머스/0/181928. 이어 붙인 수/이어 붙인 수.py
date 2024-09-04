def solution(num_list):
    odd_num_list = [num for num in num_list if num % 2]
    even_num_list = [num for num in num_list if not num % 2]
    answer = int("".join(list(map(str, odd_num_list)))) + int("".join(list(map(str, even_num_list))))
    
    return answer