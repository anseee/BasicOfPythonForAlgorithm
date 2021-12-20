# coding=UTF-8
# 동일한 알고리즘을 반복적으로 수행할때 중요

# global variable
c = 5

def add(a, b):
    print(a + b + c)

add(3, 7)
add(b = 3, a = 5)

print((lambda a, b: a + b)(3, 7))