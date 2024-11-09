results = []

T = int(input())

for _ in range(T):
    numbers = list(map(int, input().rstrip().split()))
    sorted_numbers = sorted(numbers)[1:-1]
    results.append(round(sum(sorted_numbers) / len(sorted_numbers)))
    
for test_case in range(T):
    print("#{} {}".format(test_case + 1, results[test_case]))