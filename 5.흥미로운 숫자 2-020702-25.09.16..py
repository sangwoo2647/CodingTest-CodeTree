## 초기 템플릿

    #파일 이름 : 5.흥미로운 숫자 2-020702-25.09.16.

#문제 이름 : 흥미로운 숫자 2

#문제 링크 : https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-interesting-numbers-2/description

#문제 사진 : 


#생각흐름:
    # 우선 for로 x~y 사이의 수 하나씩 받은 후
    #     그 수를 str로 쪼갠 후
    #         1,2 번째 숫자를 저장
    #             1. 그 숫자들과 다른 숫자 들어오면 탈락
    #             2. 그 숫자들이 둘다 2번 이상이면 탈락 
    #             3. 그 숫자가 한개이면 탈락



#코드:

cnt =0

x,y=map(int,input().split())

for i in range(x,y+1):
    ns = str(i) ## 배열화
    
    xx = [0] * 10 # 해당 수의 0~9 숫자배열

    for j in ns:
        xx[int(j)] += 1
    
    #사용된 숫자 카운트
    use_cnt = 0

    #딱 한번만 사용된 숫자 카운트
    first_use = 0

    for k in xx:
        if k > 0 :
            use_cnt += 1
        if k == 1:
            first_use += 1 

    #사용된 숫자가 2개 이고 / 한번만 카운트된 숫자가 1개이면 통과
    if use_cnt == 2 and first_use ==1:
        cnt += 1

print(cnt)

#배울점