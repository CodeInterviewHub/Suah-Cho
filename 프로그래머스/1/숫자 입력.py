# 입력값 int로 변경
n = int(input())
start = 11
line = 0

while line < n:
    line += 1
    # 출력할 수의 개수 카운트 변수
    cnt = 0
    while cnt < line:
        print(start, end=' ')
        start += 1
        cnt += 1
    # 줄바꿈
    print()

# # n번만큼 반복 -> i값은 1부터 n이 될 때까지 반복
# for i in range(1, n+1):
#     for j in range(i):
#         # i 크기 만큼 start값 출력
#         print(start, end=' ')
#         start += 1
#     # 줄바꿈
#     print()
