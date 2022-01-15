# coding=UTF-8
# 자료형
a = 1000
print(a)

a = -7
print(a)

a = 0
print(a)

# 실수형
a = 157.93
print(a)

a = -1837.2
print(a)

a = 5.
print(a)

a = -.7
print(a)

a = 1e9
print(a)

a = 75.25e1
print(a)

a = 3954e-3
print(a)

a = 0.3 + 0.6
print(a)

# 실수형은 정확하게 표현되지 못한다 
if round(a, 4) == 0.9:
    print(True)
else:
    print(False)

a = 7
b = 3

print(a / b)
print(a % b)

# 몫
print(a // b) 

# 제곱근
a = 5
b = 3
print (a ** b)

# 리스트 자료형
a = [1,2,3,4,5,6,7,8,9]
print(a)
print(a[4])

a = list()
print(a)

n = 10
a = [0] * n
print(a)

a = [1,2,3,4,5,6,7,8,9]
print(a[-1])
print(a[-3])
a[3] = 7
print(a)
print(a[1:4])

# List Comprehension
array = [i for i in range(20) if i % 2 == 1]
print(array)

array = [i * i for i in range(1, 10)]
print(array)

# 2차원 리스트 초기화
# 특정 크기를 가지는 2차원 리스트를 초기화할 때에는 리스트 컴프리헨션을 이용하자
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)

# 리스트 관련 기타 메서드
# 시간복잡도 (최악의 경우) 고려
# append() O(1)
# sort() O(NlogN)
# reverse() O(N)
# insert() O(N)
# count() O(N)
# remove() O(N)

# 리스트에서 특정 값 제거하기
a = [1,2,3,4,5,5,5]
remove_set = {3, 5}

result = [i for i in a if i not in remove_set]
print(result)

# 문자열 자료형
data = "Hello World"
print(data)

data = "Don't you know \"Python\"?"
print(data)

a = "Hello"
b = "World"
print(a + " " + b)

a = "String"
print(a * 3)

a = "ABCDEF"
print(a[2 : 4])

# 튜플 
# 그래프 알고리즘을 구현할때 자주 사용한다.
# 예) 다익스트라 알고리즘 (최단 경로)
# 우선순위 큐에 들어가는 데이터는 튜플을 이용함
# 변경하면 안되는 값이 변경되고 있지는 않은지 체크 가능
# 리스트에 비해 공간 효율적이고 원소의 성질이 다를때 주로 사용
a = (1,2,3,4)
print(a)

# 튜플에서 대입 연산자는 불가능
# a[2] = 7

# 사전 자료형
# (키, 값) 해시 테이블 이용
# 데이터의 검색 및 수정 O(1)

data = dict()
data['사과'] = 'apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'
print(data)

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재")

keyList = data.keys()
valueList = data.values()

print(keyList)
print(valueList)

for key in keyList:
    print(data[key])

# 집합 자료형
# 중복허용x, 순서x
# 데이터만 담음
# 특정 원소 존재 유무 확인 O(1)
# 특정한 데이터가 이미 등장한 적이 있는지 여부체크때 매우 유용
data = set([1,1,2,3,4,4,5])
print(data)
data = {1,1,2,3,4,4,5}
print(data)

# 집합 연산자
a = {1,2,3,4,5}
b = {3,4,5,6,7}
print(a | b) # 합집합
print(a & b) # 교집합
print(a - b) # 차집합

# add, remove 모두 O(1)
data.add(4)
data.update([5,6])
data.remove(3)

print(data)
