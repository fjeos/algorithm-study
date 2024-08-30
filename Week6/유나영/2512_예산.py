N = int(input())
cities = list(map(int, input().split()))
M = int(input())
result = 0

# 이분 탐색을 위한 시작, 끝 값, 끝 값은 도시들 중 최대 예산
start, end = 0, max(cities)
while start < end:
    # start, end 값이 경신될 때마다 total 값 초기화
    total = 0
    mid = (start + end) // 2
    # 모든 도시의 예산을 더하여 최대 예산보다 큰지, 작거나 같은지 판별
    for budget in cities:
        total += min(budget, mid)

    # 모든 도시 예산의 합이 전체 예산보다 크면 초과 -> end 값을 낮춤
    if total > M:
        end = mid - 1
    # 모든 도시 예산의 합이 전체 예산보다 작으면 예산이 남음 -> start 값을 올림
    # result: 현재까지 찾은 가능한 최대 상한액
    else:
        start = mid + 1
        result = mid

print(result)
