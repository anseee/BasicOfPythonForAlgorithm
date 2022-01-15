# deque와 Counter를 많이 사용
# deque를 이용하여 큐 구현
# 시작, 끝 부분에 데이터를 삽입 삭제 효과적

from collections import deque, Counter

data = deque([2,3,4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))

# Counter는 등장 횟수를 세는 기능
counter = Counter(['red', 'blue', 'green', 'blue', 'blue'])
print(counter['blue'])
print(dict(counter))