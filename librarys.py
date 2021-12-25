# coding=UTF-8
# https://docs.python.org/ko/3/library/index.html
# 내장함수
from itertools import permutations, combinations, product, combinations_with_replacement


result = sum([1,2,3,4,5])
print(result)

minResult = min([1,2,3,4,5])
print(minResult)

maxResult = max(7, 3, 5, 2)
print(maxResult)

evalResult = eval("(3+5) * 7")
print(evalResult)

sortedResult = sorted([9,1,8,5,4])
print(sortedResult)

reverseSortedResult = sorted([9,1,8,5,4], reverse = True)
print(reverseSortedResult)

keySortedResult = sorted([('홍길동', 35), ('이순신', 40), ('오이잉', 100)], key = lambda x: x[1], reverse = True)
print(keySortedResult)

# 모든 경우의 수를 뽑아줌
data = ['A', 'B', 'C']
permuResult = list(permutations(data, 3))
print(permuResult)

# 순서고려x 모든 경우의 조합을 계산
combResult = list(combinations(data, 2))
print(combResult)

# 원소 중복o, 모든 경우의 순열 계산
prodResult = list(product(data, repeat=2))
print(prodResult)

# 중복허용 모든 조합 구하기
replaceResult =list(combinations_with_replacement(data, 2))
print(replaceResult)



