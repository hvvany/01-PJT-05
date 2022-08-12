import sys

sys.stdin = open("_반반.txt")

# 딕셔너리로 받아서 길이 2인지, values가 2인지 확인
t = int(input())
for i in range(t):
    text_dic = dict()
    sentence = input()
    for text in sentence:
        if text in text_dic:
            text_dic[text] += 1
        else:
            text_dic[text] = 1
    if len(text_dic) == 2:
        for key in text_dic:
            if text_dic[key] == 2:
                answer = 'Yes'
            else:
                answer = 'No'
    else:
        answer = 'No'
    print(f'#{i+1} {answer}')