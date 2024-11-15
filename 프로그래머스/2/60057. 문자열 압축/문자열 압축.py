def solution(s):
    length = len(s)
    answer = length

    for cutting_unit in range(1, length // 2 + 1):
        left, right = 0, cutting_unit - 1 ### cutting_unit으로 자른 문자열의 시작, 끝 인덱스
        before, current = "", "" ### cutting_unit으로 자른 직전 문자열, 현재 문자열
        compressed_string = "" ### 압축된 문자열
        combo = 1 ### 동일한 문자열이 연속으로 등장한 횟수
        
        while right < length:
            current = s[left : right + 1]

            if left > 0:
                if before == current:
                    combo += 1
                else:
                    if combo == 1: ### 문자열이 한 번만 나타난 경우 1 생략
                        compressed_string += before
                    else:
                        compressed_string += "{}{}".format(combo, before)
                        combo = 1 ### 동일한 문자열이 연속으로 등장한 횟수 초기화
                    
            before = current
            left, right = right + 1, right + cutting_unit

        ### cutting_unit으로 잘린 마지막 문자열 처리
        if combo == 1:
            compressed_string += current
        else:
            compressed_string += "{}{}".format(combo, current)

        ### cutting_unit으로 자르고 마지막에 남은 문자열 처리
        compressed_string += s[left:]

        ### 최소 길이 갱신
        if answer > len(compressed_string):
            answer = len(compressed_string)
            
    return answer