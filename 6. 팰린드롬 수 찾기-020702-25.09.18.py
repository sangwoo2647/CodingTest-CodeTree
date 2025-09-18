## 초기 템플릿

    #파일 이름 : 팰린드롬 수 찾기-020702-25.09.18.py

#문제 이름 : 팰린드롬 수 찾기

#문제 링크 : https://www.codetree.ai/ko/trails/complete/curated-cards/test-find-the-number-of-palindrome/description

#문제 사진 : 


# #생각흐름:

#     for 로 x부터 y까지 순차 탐색
#         팰린드롬의 수인지 확인 (순서를 뒤집어서 저장한 게 같으면)
#         맞으면 카운트

#코드:

x,y=map(int,input().split())

cnt = 0

for i in range(x,y+1):
    temp = i
    reversed_temp =int(str(temp)[::-1]) #숫자 뒤집기 1234 -> 4321

    if i == reversed_temp:
        cnt += 1 

print(cnt)


#배울점