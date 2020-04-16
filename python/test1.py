n, m = list(map(int, input().split()))
graphs = [[] for _ in range(n+1)]
colors = [0 for _ in range(n+1)]
for _ in range(m):
    a, b = list(map(int, input().split()))
    graphs[a] += [b]
    graphs[b] += [a]


def dfs(colors, i, c):
    colors[i] = c
    print(colors)
    for v in graphs[i]:
        if colors[v] == c:
            return False
        elif colors[v] == 0 and not dfs(colors, i, -c):
            return False
    return True


def paint():
    for i in range(n+1):
        if (colors[i] == 0 and not dfs(colors, i, 1)):
            return False
    return True


if paint():
    print('Yes')
else:
    print('No')
