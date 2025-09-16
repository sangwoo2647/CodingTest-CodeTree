## 초기 템플릿

    #파일 이름 : 좌표평면 위의 특정 구역 2-020701-25.09.15.

#문제 이름 : 좌표평면 위의 특정 구역 2

#문제 링크 : https://www.codetree.ai/ko/trails/complete/curated-cards/intro-specific-zone-above-the-2d-coordinate-2/description

#문제 사진 : 


#생각흐름:

    # for문 돌리면서 하나씩 점 빼기
    # 그렇게 빼고 난 후 각 X값 중 가장 큰거 - 가장 작은거 = X 선분 길이나옴
    # 가장 큰 Y값 - 가장 작은 Y값 = Y 선분 길이 나옴 
    #     X*Y = 해당 3점을 포함한 직사각형 가장 작은 넓이 나옴

    # 최소 값만 가져가기 

#코드:

import sys

ans = sys.maxsize

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# print(points, x, y)

for i in range(n):
    mx, my = [],[]
    for j in range(n):
        if i==j:
            continue
        mx.append(x[j])
        my.append(y[j])

    xx = max(mx) - min(mx)
    yy = max(my) - min(my)

    xy = xx * yy

    ans = min(xy,ans)

print(ans)
         



#배울점

# 하나씩 내 생각과 코드가 대응되도록 / 막히면 일단 한글로 말하든 적어보고 그 이후 하나씩 작게 쪼개면서 구현 생각하기 