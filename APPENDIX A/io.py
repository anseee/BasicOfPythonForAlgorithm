import sys
# coding=UTF-8
# 알고리즘의 첫 번째 단계는 데이터를 입력 받는것
# 여러 개의 데이터를 입력받을 때 데이터가 공백으로 구문 되는 경우가 많음
# 문자열을 띄어쓰기로 구분하여 각각 정수 자료형의 데이터로 저장하는 코드가 매우 빈번하게 사용됨

# 전형적인 입력 코드
n = int(input())
data = list(map(int, input().split()))

data.sort(reverse = True)
print(data)

# n, m, k를 공백으로 구분하여 입력
n, m, k = map(int, input().split())
print(n, m, k)

# 입력을 빠르게 받는 방법
# input()은 느림 sys.stdin.readline.rstrip() 빠름
# rstrip()을 이용해서 공백 문자를 제거 할 수 있다.

data = sys.stdin.readline().rstrip()
print(data)

a = 1
b = 2
print(a, b) # 1 2 

# 줄바꿈 
print(a)
print(b)

# 형변환 출력
strA = str(a)
print(strA + "값")

# python3.6 이상
# f-string
# print(f"문법 사용해보자 {a}")