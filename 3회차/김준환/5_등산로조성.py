# import sys
# from pprint import pprint
# import copy



# sys.stdin = open("_등산로조성.txt")

# t = int(input())

# answer_lst = []

# for i in range(t):
#     n, k = map(int,input().split())
#     matrix = [list(map(int,input().split())) for _ in range(n)]
#     pprint(matrix)
#     # 최댓값 및 좌표 찾기
    # start_point = []     # [[0, 0], [2, 3], [2, 4]]
    # big = 0
    # for x in range(n):
    #     for y in range(n):
    #         if matrix[x][y] > big :
    #             big = matrix[x][y]
    #             start_point = [[x,y]]
    #         elif matrix[x][y] == big:
    #             start_point.append([x,y])
#     print(f'start_point : {start_point}')

#     # 4방 탐색 및 깊이 탐색
#     for start in start_point:
#         cnt = 0
#         cut_cnt = 0
#         copy_matrix = copy.deepcopy(matrix)
#         x = start[0]
#         y = start[1]


#         dx = [-1, 0, 1, 0]  # 위 오 아 왼
#         dy = [0, 1, 0, -1]
        
#         for idx in range(4):
#             sx = x + dx[idx]
#             sy = y + dy[idx]
#             print(f'sx : {sx}')
#             print(f'sy : {sy}')
#             if sx >= n or sy >= n or sx < 0 or sy > 0:
#                 continue
#             if copy_matrix[sx][sy] < copy_matrix[x][y]:
#                 x = sx
#                 y = sy
#             else:
#                 if cut_cnt == 0:
#                     # print('?????')
#                     for cut in range(1,k+1):
#                         if copy_matrix[sx][sy] - cut < copy_matrix[x][y]:
#                             x = sx
#                             y = sy
#                             copy_matrix[x][y] -= cut
#                             cut_cnt = 1
#                             break




#         answer_lst.append(cnt)
#         pprint(f'answer : {answer_lst}')
#     print(f'#{i+1} {max(answer_lst)}')


import copy
import sys
sys.setrecursionlimit(10**7)

t = int(input())
for i in range(t):
    n, k = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(n)]
    copy_matrix = copy.deepcopy(matrix)
    cnt = 0
    answer_lst = []
    
    
    def Dfs(x,y):
        print(f'x,y = {x},{y}')
        global cnt
        global cut_cnt
        dx = [-1, 0, 1, 0]  # 위 오 아 왼
        dy = [0, 1, 0, -1]
        for i in range(4) :
            nx = x + dx[i] # 4방향으로 검사함
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n : # 인덱스 초과 방지
                if copy_matrix[nx][ny] < copy_matrix[x][y] : # 현재 위치의 값 보다 작은 경우
                    copy_matrix[x][y] = 50 # 20이하 높이니까 그냥 50
                    cnt += 1
                    print('??')
                    
                    
                    Dfs(nx, ny) # 방문 한 섬에서 dfs실행
                    
                else:
                    if cut_cnt == 0:   # 컷 아이템을 사용한 적이 없으면
                        for cut in range(1,k+1):
                            if copy_matrix[nx][ny] - cut < copy_matrix[x][y]:
                                copy_matrix[nx][ny] -= cut
                                cnt = 1
                                print('?')
                                cut_cnt += 1
                                Dfs(nx,ny)
                            else:
                                
                    else:
                        cut_cnt.append(1)
                        return


    start_point = []     # [[0, 0], [2, 3], [2, 4]]
    big = 0
    for x in range(n):
        for y in range(n):
            if matrix[x][y] > big :
                big = matrix[x][y]
                start_point = [[x,y]]
            elif matrix[x][y] == big:
                start_point.append([x,y])
    print(start_point)

    for start in start_point:
        i = start[0]
        j = start[1]
        cnt = 0
        cut_cnt = [0]
        print(f'i, j : {i},{j}')
        Dfs(i, j)
        answer_lst.append(cnt)
    print(max(answer_lst))