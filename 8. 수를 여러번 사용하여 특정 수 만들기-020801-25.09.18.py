## 초기 템플릿

    #파일 이름 : 8. 수를 여러번 사용하여 특정 수 만들기-020801-25.09.18

#문제 이름 : 수를 여러번 사용하여 특정 수 만들기

#문제 링크 : https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-create-a-specific-number-using-multiple-numbers/description

#문제 사진 : 


#생각흐름:

    # 1 2
    # 2 1 

    # 1 3

    # 3 1 

    # 5 1

    # 12 2 -> 이걸 순차로 도는 법을 모르겠엄

    # a가 
    # 1번 하고 나머지
    # 2번 하고 나머지
    # 3번 하고 나머지...  => 순서를 생각했어야하함함

#코드:
ans =0

a,b,c = map(int,input().split())


for i in range( (c//a)+1):
    remain = c - (a*i) #처음 a 만큼 덜어내기 (1번2번... a//c번까지)

    j = remain//b #그렇게 남은 remain에 대해 b는 최대 j번까지 나눌 수 있음 
    xx = remain - (b*j) # 최대 j번까지 나눌 수 있으니까 해당 값 뺴기 
    
    # xx 는 지금 c와 a,b로 만들 수 있는 수의 격차 
    tmp = c 
    tmp -= xx

    ans = max(ans,tmp) #할 수 있는 가장 큰 수 즉 가장 인접해있는 수 취득 


print(ans)

#배울점