A, B = map(str, input().split())
min_value = 0
max_value = 0

min_value = int(A.replace('6', '5')) + int(B.replace('6', '5'))
max_value = int(A.replace('5', '6')) + int(B.replace('5', '6'))
print(min_value, max_value)