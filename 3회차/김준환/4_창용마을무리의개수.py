import sys

sys.stdin = open("_창용마을무리의개수.txt")

t = int(input())
for i in range(t):
    n, m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    for _ in range(m):
        idx1, idx2 = map(int,input().split())
        graph[idx1].append(idx2)
        graph[idx2].append(idx1)
    
    stack = []
    cnt = 0
    for num in range(1,n+1):
        if visited[num] == False:
            visited[num] = True
            stack.append(num)

            while stack:
                current = stack.pop()
                for n in graph[current]:
                    if visited[n] == False:
                        visited[n] = True
                        stack.append(n)

            cnt += 1
    print(f'#{i+1} {cnt}')