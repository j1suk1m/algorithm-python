T = int(input())

def isPalindrome(word: str) -> int:
    left = 0
    right = len(word) - 1
    
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            return 0
        
    return 1
    
results = []
for _ in range(T):
    word = input().rstrip()
    results.append(isPalindrome(word))

for test_case in range(T):
    print("#{} {}".format(test_case + 1, results[test_case]))