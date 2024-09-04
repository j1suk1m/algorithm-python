from sys import stdin

input = lambda: stdin.readline().rstrip()

string1 = "-" + input()
string2 = "-" + input()
length1 = len(string1)
length2 = len(string2)
dp = [[0] * length2 for _ in range(length1)]
LCS_length = 0

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