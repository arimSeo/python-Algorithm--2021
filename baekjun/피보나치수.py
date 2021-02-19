#----Question.
# 피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.
# 이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.
# n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

#----Sol1) 시간초과..
a=int(input())
def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else: return fibo(n-1)+fibo(n-2) 
print(fibo(a))

# ====Sol2)
n=int(input())
ans=0; f0=0; f1=1
if n<2:
    print(n)
else:
    for i in range(1,n):
        ans=f1+f0
        f0=f1
        f1=ans
    print(ans)  

