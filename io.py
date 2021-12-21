# coding=UTF-8
# 알고리즘의 첫 번째 단계는 데이터를 입력 받는것
# 여러 개의 데이터를 입력받을 때 데이터가 공백으로 구문 되는 경우가 많음
# 문자열을 띄어쓰기로 구분하여 각각 정수 자료형의 데이터로 저장하는 코드가 매우 빈번하게 사용됨

# 전형적인 입력 코드
n = int(input())
data = list(map(int, input().split()))

data.sort(reverse = True)
print(data)