# coding=UTF-8
# whilte
# 조건이 참일때까지 반복

i = 1
result = 0

while i <= 9:
    result += 1
    i += 1

print(result)

i = 1
result = 0

# 홀수만 더하기
while i <= 9:
    if i % 2 == 1:
        result += 1
    i += 1

print(result)

# for 문
result = 0

for i in range(1, 10):
    result += 1

print(result)

# 리스트나 튜플 데이터의 모든 원소를 첫 번째 부터 방분할때는 range(n)을 사용한다.

scores = [90, 85, 77, 65, 97]

for i in range(5):
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격 입니다")

# continue를 사용하면 프로그램의 흐름은 반복문의 처음으로 돌아간다.
cheatingList = {2,4}

for i in range(5):
    if i + 1 in cheatingList:
        continue
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격 입니다")

# 반복문 중첩 가능
for i in range(2, 10):
    for j in range(1, 10):
        print(i, "X", j, "=", i * j)
    print()