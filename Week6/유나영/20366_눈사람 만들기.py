N = int(input())
snowballs = list(map(int, input().split()))
snowballs.sort()
snowman = []
for i in range(N):
    for j in range(i + 1, N):
        snowman.append((i, j, snowballs[i] + snowballs[j]))

snowman.sort(key=lambda x: x[2])
answer = 1e9
length = len(snowman)
for i in range(length-1):
    elza_head, elza_body, elza_height = snowman[i]
    anna_head, anna_body, anna_height = snowman[i+1]
    if elza_head != anna_head and elza_body != anna_body and elza_head != anna_body and elza_body != anna_head:
        answer = min(answer, anna_height - elza_height)

print(answer)