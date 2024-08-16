from sys import stdin

input = lambda: stdin.readline().rstrip()

N, M = map(int, input().split())
chapters = [(0, 0)] + list(tuple(map(int, input().split())) for _ in range(M))
dp = [[0] * (N + 1) for _ in range(M + 1)]

### 배낭 문제
for chapter in range(1, M + 1):
    for day in range(1, N + 1):
        chapter_day, chapter_page = map(int, chapters[chapter])
        
        if day < chapter_day:
            dp[chapter][day] = dp[chapter - 1][day]
        else:
            dp[chapter][day] = max(dp[chapter - 1][day], dp[chapter - 1][day - chapter_day] + chapter_page)

print(dp[M][N])