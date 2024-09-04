from sys import stdin

input = lambda: stdin.readline().rstrip()

string1 = "-" + input()
string2 = "-" + input()
length1 = len(string1)
length2 = len(string2)
dp = [[0] * length2 for _ in range(length1)]
LCS_length = 0
LCS = ""

### 최장 공통 문자열
for index1 in range(1, length1):
    for index2 in range(1, length2):
        char1 = string1[index1]
        char2 = string2[index2]
        
        if char1 == char2:
            dp[index1][index2] = dp[index1 - 1][index2 - 1] + 1
        else:
            dp[index1][index2] = max(dp[index1 - 1][index2], dp[index1][index2 - 1])
            
        LCS_length = max(LCS_length, dp[index1][index2])
        
print(LCS_length)
    
if LCS_length > 0:
    index1 = length1 - 1
    index2 = length2 - 1
    
    while dp[index1][index2] > 0:
        current = dp[index1][index2]
        
        if index1 >= 1 and dp[index1 - 1][index2] == current:
            index1 -= 1
        elif index2 >= 1 and dp[index1][index2 - 1] == current:
            index2 -= 1
        else:
            LCS += string1[index1]
            index1 -= 1
            index2 -= 1           

    print(LCS[::-1])