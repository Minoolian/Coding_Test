def dfs(rday, rmin, satis, last_visit):
    found_points = False
    for i, (m, s) in points.items():
        if visited[i]:
            continue
        if rmin - m - distance[last_visit][i] >= 10:
            found_points = True
            path.append(i)
            visited[i] = 1
            dfs(rday, rmin - m - distance[last_visit][i], satis + s, i)
            path.pop()
            visited[i] = 0
    if not found_points:
        if rday > 1:
            for i in hotels:
                if distance[last_visit][i] <= rmin:
                    path.append(i)
                    dfs(rday-1, 540, satis, i)
                    path.pop()
        else:
            if rmin >= distance[last_visit][airport] and ans[0] < satis:
                ans[0] = satis
                ans[1] = path[1:] + [airport]


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    distance = [[0]*(N+1) for _ in range(N+1)]
    for i in range(1, N):
        line = list(map(int, input().split()))
        for j, d in enumerate(line, i+1):
            distance[i][j] = distance[j][i] = d
    hotels = []
    points = {}
    for i in range(1, N+1):
        line = input()
        if line[0] == 'P':
            points[i] = list(map(int, line.split()[1:]))
        elif line[0] == 'H':
            hotels.append(i)
        else:
            airport = i
    ans = [0, []]
    visited = [0]*(N+1)
    path = [airport]
    dfs(M, 540, 0, airport)
    print('#{} {} {}'.format(tc, ans[0], ' '.join(map(str, ans[1]))))