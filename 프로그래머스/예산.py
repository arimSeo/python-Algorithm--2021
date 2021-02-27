#----Question
#전체 예산이 정해져 있기 때문에 모든 부서의 물품을 구매해 줄 수는 없습니다. 
#그래서 최대한 많은 부서의 물품을 구매해 줄 수 있도록 하려고 합니다.
#물품을 구매해 줄 때는 각 부서가 신청한 금액만큼을 모두 지원해 줘야 합니다. 
#예를 들어 1,000원을 신청한 부서에는 정확히 1,000원을 지원해야 하며, 1,000원보다 적은 금액을 지원해 줄 수는 없습니다.
#부서별로 신청한 금액이 들어있는 배열 d와 예산 budget이 매개변수로 주어질 때,
# 최대 몇 개의 부서에 물품을 지원할 수 있는지 return 하도록 solution 함수를 완성해주세요.

def solution(d, budget):
    money=0        # money==지원가능 총액수
    result=0
    d.sort()
    for i in range(0,len(d)):
        if d[i]+money<=budget:        #지원 총액수<=budget 일때
            money=money+d[i]      #현재 지원가능한 총액수 저장
            result+=1             #결과는 부서개수 result          
    return result

print(solution([1,3,2,5,4],9))  #결과값 : 3