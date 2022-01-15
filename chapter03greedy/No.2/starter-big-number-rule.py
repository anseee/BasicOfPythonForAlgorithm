# 가장 큰 수를 뽑는다
# k번까지 더한다
# k번까지 끝내면 그 다음 큰 수를 찾아서 한번 더한다
# 다시 제일 큰 수를 k번까지 더한다

n = 5 # 배열 크기
m = 8 # 숫자가 더해지는 횟수
k = 3 # 큰 수를 더 할 수 있는 최대 수
list = [2, 4, 5, 4, 6]
result = 0

firstMax = max(list)
list.remove(firstMax)
secondMax = max(list)

for i in range(m):
    if (i + 1) % (k + 1) == 0:
        result += secondMax
    else:
        result += firstMax
    
print(result)