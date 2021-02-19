#----QUESTION.
# 일곱 난쟁이의 키의 합이 100이 됨을 기억해 냈다.
# 아홉 난쟁이의 키가 주어졌을 때, 일곱 난쟁이를 찾는 프로그램을 작성하시오.
# 아홉 개의 줄에 걸쳐 난쟁이들의 키가 주어진다. 주어지는 키는 100을 넘지 않는 자연수이며, 아홉 난쟁이의 키는 모두 다르며, 가능한 정답이 여러 가지인 경우에는 아무거나 출력한다.
# 일곱 난쟁이의 키를 오름차순으로 출력한다. 일곱 난쟁이를 찾을 수 없는 경우는 없다.

#----Sol.
lst=[]
for i in range(9):
    # m= int(input())
    # lst=list(m)
    lst.append(int(input()))
    lst.sort()
    res= sum(lst)
for i in range(9):
    for j in range(i+1,9):
        # lst[i]중 7개 합이 100
        if res-lst[i]-lst[j]==100:
            for k in range(9):
                if k==i or k==j:        #두개 제외
                    pass
                else: print(lst[k])
            exit()
            
