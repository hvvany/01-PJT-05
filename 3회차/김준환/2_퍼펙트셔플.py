import sys
from collections import deque

sys.stdin = open("_퍼펙트셔플.txt")


t = int(input())
for i in range(t):
    l = int(input())
    input_lst = list(input().split())
    if l % 2 == 0:
        last_idx = l // 2
    else:
        last_idx = l // 2 + 1
    first_lst = input_lst[0:last_idx]
    second_lst = input_lst[last_idx:]
    idx = 1
    for text in second_lst:
        first_lst.insert(idx,text)
        idx += 2
    print(f'#{i+1} ',end='')
    for answer in first_lst:
        print(answer,end=' ')
    print()