import sys

sys.stdin = open("_모음이보이지않는사람.txt")

t = int(input())
for i in range(t):
    sentence = input()
    print(f'#{i+1} ',end='')
    for text in sentence:
        if text in 'aeiou':
            print('',end='')
        else:
            print(text,end='')
    print()