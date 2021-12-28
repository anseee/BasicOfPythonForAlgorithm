from random import randint
import time

def select_sort():
  arr = [randint(1, 100) for i in range(10)]

  start_time = time.time()

  for i in range(len(arr)):
    min_index = i

    for j in range(i + 1, len(arr)):
      if arr[min_index] > arr[j]:
        min_index = j
        
    arr[i], arr[min_index] = arr[min_index], arr[i]

  end_time = time.time()
  print("선택정렬 성능 측정:", end_time - start_time)

def default_sort():
  arr = [randint(1, 100) for i in range(10)]

  start_time = time.time()

  arr.sort()

  end_time = time.time()

  print("기본 정렬 성능 측정:", end_time - start_time)
