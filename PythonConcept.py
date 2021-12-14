
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
'''
#중첩if문
x = 12
if x>=10:
    if x%2 == 1:
        print("10 이상의 홀수")
x = 9
if x>0:
    if x<10:
        print("10보다 작은 자연수")
x=7
if x>0 and x<10:
    print("10보다 작은 자연수")

x=7
if 0<x<10:
    print("10보다 작은 자연수")

x=int(input("숫자를 입력하세요 : "))
if x>0:
    print("양수")
else:
    print("음수")


x=50
if x>=90: #첫번째 참에서 걸러진다
    print('A')
elif x>= 80:
    print('B')
elif x>=70:
    print("C")
elif x>=60:
    print("D")
else:
    print("F")
'''

'''
a=range(1, 11)
print(list(a))
for i in range(1, 10): #i증가
    print(i)
for i in range(10, -1, -2):#i -2만큼 감소
    print(i)
'''
'''
i=1
while i<=10:
    print(i)
    i=i+1
i=10
while i>=1:
    print(i)
    i=i-1
'''

'''
i=1
while True:
    print(i)
    if i==10:
        break
    i+=1
'''

'''
for i in range(1, 11):
    if i%2==0:
        continue #조건 참이 되면 아래는 skip한다
    print(i)
'''
'''
for i in range(1, 11):
    print(i)
    if i>=15:
        break
else:
    print(11) #break되지 않을 때 else구문도 출력된다.
'''

'''
#1. 1부터 N까지 홀수출력하기

n = int(input("숫자를 입력하세요 : "))
for i in range(1, n+1):
    if i%2==1:
        print(i)


#2. 1부터 N까지의 합 구하기

n = int(input("숫자를 입력하세요 : "))
i = 1
sum = 0
while i<=n:
    sum += i
    i += 1
print(sum)



#3. N의 약수 출력하기

n = int(input("숫자를 입력하세요 : "))
for i in range(1, n+1):
    if n%i == 0:
        print(i, end = ' ') #옆에 붙어 나오게 함
'''

#중첩 반복문
'''
for i in range(5):
    for j in range(5):
        print(j, end= ' ')
    print()


for i in range(5):
    for j in range(5-i):
        print("*", end = '')
    print()
'''

'''
문자열 및 내장함수
a="It is Time"
print(a.upper()) #대문자화 시켜서 출력, 문자열 변경은 하지않음
print(a.lower())
print(a)
tmp=a.upper()
print(tmp)
print(tmp.find('T'))#가장 첫번째 인덱스값 반환
print(tmp.count('T'))
print(a[:2]) #인덱스 2번 전까지
print(a[3:5]) #3번부터 4번까지만
print(len(a))

for i in range(len(a)):
    print(a[i], end=' ')
print()

for x in a: #x는 a 문자열의 개별 문자
    print(x, end = ' ')
print()
for x in a:
    if x.isupper(): #isuppper함수는 대문자인 경우 1 반환
        print(x, end=' ')
print()

for x in a:
    if x.isalpha(): #알파벳인경우 (공백은 False)
        print(x, end='')
print()

tmp='AZaz'
for x in tmp:
    print(ord(x)) #ord는 ASCII 반환 함수
tmp=65
print(chr(tmp))
'''

#리스트와 내장함수

#import random as r 셔플 사용위해 import
'''
b=list()
#print(b)

a = [1, 2, 3, 4, 5]
#print(a)
#print(a[0])

b=list(range(1,11))
#print(b)
c=a+b
#print(c)

print(a)
a.append(6)#a 리스트 맨 뒤에 6 추가
print(a)

a.insert(3,7)#a 인덱스 3번 인덱스에 7 추가, 기존 3번 인덱스는 4번으로 밀림
print(a)

a.pop() #리스트에서 맨 뒤의 값 제거
print(a)

a.pop(3) #리스트에서 3번 인덱스의 값 제거
print(a)

a.remove(4) #4라는 값을 찾아서 제거
print(a)

print(a.index(5))
a=list(range(1,11))
print(a)
print(sum(a))
print(max(a))
print(min(a))
print(min(7, 3, 5))

r.shuffle(a)
print(a)
a.sort() #오름차순 정렬
print(a)
a.sort(reverse=True) #내림차순 정렬
print(a)
a.clear()
print(a)
'''

'''
a = [23, 12, 36, 53, 19]
print(a[:3]) #0부터 2까지 출력
print(a[1:4])
print(len(a))

for i in range(len(a)):
    print(a[i], end = ' ')
print()

for x in a:
    if x%2 == 1:
        print(x, end = ' ')
print()

for x in enumerate(a): #(인덱스 번호, 저장값) 반환 (튜플 형태 자료구조)
    print(x[0], x[1], sep=' ')
print()

for index, value in enumerate(a):
    print(index, value)
print()
'''
'''리스트와 튜플의 차이점
b=(1, 2, 3, 4, 5)
print(b[0])
b[0]=7
print(b[0])
튜플은 값 변경을 하려면 에러가 발생.
'''
'''
if all(50>x for x in a): #all 안에 조건 모두 만족시에만 True 반환
    print("YES")
else:
    print("NO")

if any(15>x for x in a): #any 안에 조건 한번이라도 만족시 True 반환
    print("YES")
else:
    print("NO")
'''

'''
#2차원 리스트 생성과 접근
a=[0]*3 #[0,0,0] 리스트 생성
print(a)
a=[[0]*3 for _ in range(3)]
print(a)
a[0][1]=1
a[1][1]=2
print(a)

for x in a:
    print(x)

for x in a:
    for y in x:
        print(y, end = ' ')
    print()
'''

#함수 만들기 - main script 위에 만들어야함!
'''
def add(a, b):
    c=a+b
    print(c)
add(3, 2)
add(5, 7)

def add(a, b):
    c=a+b
    return c
print(add(3, 2))

def add(a, b):
    c=a+b
    d=a-b
    return c, d #tuple로 갯수 상관없이 return 가능
print(add(3, 2))


def isPrime(x):
    for i in range(2, x):
        if x%i==0:
            return False
    return True

a=[12, 13, 7, 9, 19]
for k in a:
    if isPrime(k):
        print(k, end=' ')
'''

'''
#람다 함수/람다 표현식
def plus_one(x):
    return x+1
print(plus_one(1))

plus_two=lambda x: x+2
print(plus_two(1))

def plus_one(x):
    return x+1
a=[1, 2, 3]
print(list(map(plus_one, a)))
print(list(map(lambda x: x+1, a)))
'''
