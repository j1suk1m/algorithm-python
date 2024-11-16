def reverse_direction(string: str) -> str:
    if string == "":
        return string
    else:
        reversed_string = ""
        
        for char in string:
            if char == "(":
                reversed_string += ")"
            else:
                reversed_string += "("
                
        return reversed_string
    
def is_correct(string: str) -> bool:
    count = 0
    
    for idx in range(len(string)):
        char = string[idx]
        
        if char == "(":
            count += 1
        else:
            count -= 1
            
        if count < 0:
            return False
        
    return count == 0

def get_balanced_end(string: str) -> int:
    count = 0
    idx = 0
    
    for idx in range(len(string)):
        char = string[idx]
        
        if char == "(":
            count += 1
        else:
            count -= 1
        
        if count == 0:
            return idx
    
    return idx - 1
    
def solution(p):
    if p == "" or is_correct(p):
        return p
    
    split_idx = get_balanced_end(p)
    u, v = p[:split_idx+1], p[split_idx+1:]
    
    if is_correct(u):
        return u + solution(v)
    else:
        return "(" + solution(v) + ")" + reverse_direction(u[1:-1])