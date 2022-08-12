import sys

sys.stdin = open("_Flatten.txt")


t = 10  #테스트 케이스 10개

for i in range(t):
    n = int(input())
    input_lst = list(map(int,input().split()))
    for _ in range(n):
        max_idx = input_lst.index(max(input_lst))
        min_idx = input_lst.index(min(input_lst))
        input_lst[max_idx] -= 1
        input_lst[min_idx] += 1
    print(f'#{i+1} {max(input_lst) - min(input_lst)}')