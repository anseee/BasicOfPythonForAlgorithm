import sys

money = int(sys.stdin.readline().rstrip())
count = 0

count += money // 500
money = money % 500

count += money // 100
money = money % 100

count += money // 50
money = money % 50

count += money // 10

print(count)

