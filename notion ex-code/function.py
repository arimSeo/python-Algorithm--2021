# 함수(function)-----------
#
def add(a,b):     #메소드 내에서만 허용되는 변수(지역변수)
    print("%d, %d의 합은 %d" %(a,b,a+b))
a=add(3,4)
print(a)

#
def add(a,b):
	return 2*a+b
print(add(b=5,a=3))

#
def many(*args):
	result=0
	for i in args:
		result=result+i
	return result
res= many(1,2,3)
print(res)

#
def keyward(**kwargs):
	return kwargs
print(keyward(a=1,name='arim'))

#
def result(one,two):
	return one+two, one*two
result(1,3)

def me(name,old,man=True):      # man=True로 매개변수 초기값 설정
	print("이름은 %s" %name)
	print("나이는 %d살" %old)
	if man: print("남자")
	else: print("여자")
me("arim",24) 


# 
# ※ lambda 예약어로 만든 함수는 return 명령어가 없어도 결괏값을 돌려준다.
add= lambda a,b: a+b
print(add(3,4))
