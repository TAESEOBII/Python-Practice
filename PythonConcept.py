
'''
값 교환
a, b = 10, 20
print(a, b)
a, b = b, a
print(a, b)
'''

'''
#변수타입
a = 1234512345362
print(type(a))
a = 12.122485214881910103516617 #실수는 8바이트(64비트) 까지만 저장 가능
print(type(a))
a = 'student' #작은따옴표 쌍따옴표 상관없음
print(type(a))
'''

'''
#출력방식
print("number")
a, b, c = 1, 2, 3
print(a, b, c)
print("number :", a, b, c)
print(a, b, c, sep = '\n') #sep은 변수 사이를 구분하게 한다. sep 없으면 붙어나옴
print(a, end = ' ')
print(b, end = ' ')
print(c)
'''

'''
#변수입력과 연산자
a = input("숫자를 입력하세요 : ")
print(a)
'''

'''
a, b = input("숫자를 입력하세요 : ").split()
print(type(a))
c=a+b
print(type(c))
print(c)


a, b = input("숫자를 입력하세요 : ").split()
a = int(a)
b = int(b)
print(type(a))
print(a+b)
'''

'''
a, b = map(int, input("숫자를 입력하세요 : ").split())
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
'''
