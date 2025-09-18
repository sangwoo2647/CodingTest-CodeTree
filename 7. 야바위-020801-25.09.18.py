## 초기 템플릿

    #파일 이름 : 7. 야바위-020801-25.09.18.py

#문제 이름 : 야바위

#문제 링크 : https://www.codetree.ai/ko/trails/complete/curated-cards/intro-ya-rock/description

#문제 사진 :
 
    # 종이컵 객체 3개 생성

    # 종이컵 구성(진짜번호, 조약돌유뮤)
    #     진짜번호
    #     현재위치
    #     조약돌유무

    # for로 각 1,2,3 컵에 조약돌 넣는다고 구현
    #     1번 조약돌일시 몇번 점수를 얻냐 --- 반복

    # 최대점수인 위치 출력력


#생각흐름:


#코드:
ans =0
n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]
a, b, c = zip(*moves)
a, b, c = list(a), list(b), list(c)

for i in range(1,4):
    start = i
    score = 0

    for j in range(n):
        if start == a[j]:
            start =b[j]
        elif start == b[j]:
            start = a[j]
        
        if start == c[j]:
            score +=1
    ans = max(score,ans)

print(ans)



# #배울점
# 조약돌이 들어있는 컵이 바뀌는게 아니면 굳이 바꾸는걸 표시할 필요가 없음을 고려하자 -> 쓸모없는 복잡성을 내가 고려하고 있는건 아닌지 생각하자