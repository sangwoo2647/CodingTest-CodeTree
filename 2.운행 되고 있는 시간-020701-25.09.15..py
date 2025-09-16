## 초기 템플릿

    #파일 이름 : 2.운행 되고 있는 시간-020701-25.09.15.

#문제 이름 : 운행 되고 있는 시간

#문제 링크 : https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-hours-in-service/description

#문제 사진 : 


# #생각흐름:
#     반복 돌려서 한명씩 잘랐을 때 모든 경우의 수 구하기 

#         짜른 후 아무도 일 안하는 시간이 가장 적은 경우 (즉 시간 배열의 값이 0이 가장 적은 경우)
#         의 시간만 취득

#     최대값만 가지기


#코드:

import sys

ans = -sys.maxsize

n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
a = [t[0] for t in times]
b = [t[1] for t in times]


for i in range(n):
    time = [0] *  1001
    cnt = 0
    for j in range(n):
        if i == j:
            continue
    
    
        for k in range (a[j], b[j]):
            time[k] +=1
    print(time)

    for m in range(1001):
        if time[m] !=0:
            cnt +=1
    
    ans = max(ans,cnt)

print(ans)



#배울점