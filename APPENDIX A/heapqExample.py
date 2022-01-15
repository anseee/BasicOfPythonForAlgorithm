import heapq

# 다익스트라 최단 경로 알고리즘을 포함하여
# 다양한 알고리즘에서 우선순위 큐 기능을 구현하고자 할때 사용
# 최소 힙으로 구성 되어있음 O(NlogN)
# 파이썬에서는 최대 힙은 제공하고 있지 않음
# 최대힙을 구현하려면 원소의 부호를 임시로 꺼낸 뒤에 다시 원소의 부호를 변경하면 됨.

def heapsort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, -value)

    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)
