# coding=UTF-8
# 조건문
x = 15

if x >= 10:
    print(x)

score = 85

if score >= 90:
    print("학점 A:")
elif score >= 80:
    print("학점 B")
elif score >= 70:
    print("학점 C")
else:
    print("학점 F")

# 비교 연산자
x = 5
y = 4

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# 논리 연산자

print(x and y)
print(x or y)
print(not x)

# 기타 연산자
# 리스트 안에 x값이 있으면 true
print (x in [1,2,3,4,5])
print (x not in [1,2,3,4,5])

# 조건문에서 아무것도 처리하고 싶지 않을때 pass
score = 85

if score >= 80:
    pass
else:
    print("성적이 80점 미만")

# 조건부 표현식
result = "Success" if score >= 80 else "Fail"
print(result)