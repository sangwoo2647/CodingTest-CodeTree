## 초기 템플릿

    #파일 이름 : 3.스승의 은혜3-250701-25.09.16

#문제 이름 : 스승의 은혜3

#문제 링크 : https://www.codetree.ai/ko/trails/complete/curated-cards/test-the-grace-form-teacher-3/description

#문제 사진 : 


#생각흐름:
    # 누가 반값될껀지 하나씩 다 돌림
    #   가장 값이 작은 순으로 정렬 후 
    #       앞에서부터 예산에 맞게 가져가보기
    #          최대명수만 가져가기


#코드:


# 입력 받기
N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]

max_students = 0  # 선물 가능한 '최대 학생 수'

# i번째 학생의 선물을 할인하는 모든 경우를 시도
for i in range(N):
    
    # 1. 이번 경우에 사용할 '총비용' 리스트를 매번 새로 생성
    costs = []
    for j in range(N):
        p, s = gifts[j]
        
        # i번째 학생이면 가격을 50% 할인하여 총비용 계산
        if i == j:
            costs.append((p // 2) + s)
        # 다른 학생들은 원래 가격으로 총비용 계산
        else:
            costs.append(p + s)
            
    # 2. '총비용' 리스트를 오름차순으로 정렬 (핵심!)
    costs.sort()
    
    # 3. 예산 내에서 최대한 많은 선물 구매하기
    current_budget = B
    student_count = 0
    
    for cost in costs:
        # 이 선물을 살 돈이 있는지 먼저 확인
        if current_budget >= cost:
            current_budget -= cost
            student_count += 1
        else:
            break
            
    # 4. 이번 경우의 학생 수를 역대 최댓값과 비교하여 갱신
    max_students = max(max_students, student_count)

print(max_students)






#배울점
    # 물건 값과 배송비를 합쳐서 핸들링하는 방향으로 해야 안복잡해짐 
    # 가장 많은 물건을 담을려면 작은 것부터 담아야한다라는 사실을 기억하기