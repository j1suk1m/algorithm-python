def compress(s, cutting_unit, length):
    chunks = [s[idx : idx + cutting_unit] for idx in range(0, length, cutting_unit)] + ["END"]
    combo = 1 ### 문자열의 연속 횟수
    result = 0 ### 압축된 문자열의 길이
    
    for idx in range(1, len(chunks)):
        previous = chunks[idx - 1]
        current = chunks[idx]
        
        if previous == current: ### 문자열이 연속된 경우
            combo += 1
        else:
            if combo == 1:
                result += len(previous)
            else:
                result += len(str(combo)) + len(previous)
                combo = 1
    
    return result

def solution(s):
    length = len(s)
    answer = length
    
    ### 문자열 분할 단위를 늘려가며 압축 시도
    for cutting_unit in range(1, length // 2 + 1):
        answer = min(answer, compress(s, cutting_unit, length))
        
    return answer