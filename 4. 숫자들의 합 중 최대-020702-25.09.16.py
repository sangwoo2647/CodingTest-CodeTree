## 초기 템플릿

    #파일 이름 : 4. 숫자들의 합 중 최대-020702-25.09.16

#문제 이름 : 숫자들의 합 중 최대

#문제 링크 : https://www.codetree.ai/ko/trails/complete/curated-cards/intro-maximum-of-sum-of-numbers/description

#문제 사진 : 


#생각흐름:

    # for로 x이상 y 이하의 수를 가져와서 
    #     str로 처리해서 각 자리수 취득 
    #     그 자리 수들을 합쳐서  최대인거 취득

#코드:

ans =0
x,y = map(int,input().split())

for i in range(x,y+1):
    sum = 0
    ss = str(i)
    for j in range(len(ss)):
        sum += int(ss[j])

        ans = max(sum,ans)
    
print(ans)



#배울점