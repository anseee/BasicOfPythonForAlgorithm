# 가장 큰 수와 두 번째로 큰 수만 저장하면 된다.
# 최대 k번이므로, 가장 큰 수를 k번 더하고 두 번째로 큰 수를 한번 더하는 연산 처리

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

# result = 0

# while True:
#     for i in range(k):
#         if m == 0:
#             break
        
#         result += first
#         m -= 1

#     if m == 0:
#         break
#     result += second
#     m -= 1

count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += count * first
result += (m - count) * second

print(result)


