from bisect import bisect_left, bisect_right

# 이진탐색 라이브러리
# 정렬된 배열에서 특정 원소 찾을때 효과적
# 아래 두 메서드는 정렬된 순서를 유지하면서 
# 리스트에 데이터를 삽입할 왼쪽 오른쪽 인덱스를 찾는 메서드

a = [1,2,4,4,8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))

# 정렬된 리스트에서 값이 특정 범위에 속하는 원소의 갯수를 
# 구할때 효과적

def countByRange(a, leftValue, rightValue):
    rightIndex = bisect_right(a, rightValue)
    leftIndex = bisect_left(a, leftValue)
    
    return rightIndex - leftIndex

b = [1,2,3,3,3,3,4,4,8,9]

# 값이 4 인 데이터 갯수 출력
print(countByRange(b, 4, 4))

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(countByRange(b, -1, 3))