"""
문제
[9, 4, 3, 1, 12]을 오름차순으로 정렬하시오. 

---------------------------- 주어진 위치 = 0번 인덱스 ------------------------------

1. 최소값 찾기
- 0번 인덱스의 값은 9입니다. 현재까지는 9가 최소값입니다. 
- 1번 인덱스의 값 4와 최소값을 비교합니다. 4는 9보다 작으므로 4가 최소값입니다. 
- 2번 인덱스의 값 3과 최소값을 비교합니다. 3은 4보다 작으므로 3이 최소값입니다. 
- 3번 인덱스의 값 1과 최소값을 비교합니다. 1은 3보다 작으므로 1이 최소값입니다. 
- 4번 인덱스의 값 12와 최소값을 비교합니다. 1은 12보다 작으므로 1이 최소값입니다. 
- 최소값은 3번 인덱스의 1입니다. 

2. 최소값을 0번 인덱스에 배치하기 
- 3번 인덱스의 1을 0번 인덱스로 옮기고, 
  0번 인덱스의 9를 3번 인덱스로 옮깁니다. 

3. 결과
[1, 4, 3, 9, 12]
0번 인덱스까지 정렬되었습니다.

--------------------------- 주어진 위치 = 1번 인덱스 -----------------------------

1. 최소값 찾기 
- 1번 인덱스의 값은 4입니다. 현재까지는 4가 최소값입니다. 
- 2번 인덱스의 값은 3입니다. 3은 4보다 작으므로 3이 최소값입니다. 
- 3번 인덱스의 값은 9입니다. 3은 9보다 작으므로 3이 최소값입니다. 
- 4번 인덱스의 값은 12입니다. 3은 12보다 작으므로 3이 최소값입니다. 
- 최소값은 2번 인덱스의 3입니다. 

2. 최소값을 1번 인덱스에 배치하기 
- 2번 인덱스의 3을 1번 인덱스로 옮기고, 
  1번 인덱스의 4를 2번 인덱스로 옮깁니다. 

3. 결과
[1, 3, 4, 9, 12]
1번 인덱스까지 정렬되었습니다. 

--------------------------- 주어진 위치 = 2번 인덱스 -----------------------------
반복

--------------------------- 주어진 위치 = 3번 인덱스 -----------------------------
반복

--------------------------- 주어진 위치 = 4번 인덱스 -----------------------------
반복


결과
[1, 3, 4, 9, 12]

"""
  # 0번과 1~n까지 비교 후 최소값 0번 자리에 넣기
  # 1번과 2~n까지 비교 후 최소값 1번 자리에 넣기
  # ...
  # n-1번과 n-1~n까지 비교 후 최소값 n-1번 자리에 넣기

  # if n-1 전에 교환이 끝나면 stop?

def selection_sort(list):
      
    length = len(list)

    for i in range(length-1):
        stop = 0

        for j in range(i,length):
            if list[i] > list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
                stop += 1

        if stop == 0:
              break

    return list


list = [9, 4, 3, 1, 12]
# list = [9, 4, 3, 1, 12, 2, 8, 5, 10]
print(selection_sort(list))