# coding=UTF-8
# https://docs.python.org/ko/3/library/index.html
# 내장함수

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
