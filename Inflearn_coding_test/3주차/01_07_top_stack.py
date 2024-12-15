top_heights = [6, 9, 5, 7, 4]

## 단순 반복문을 통해 푼 버전
# def get_receiver_top_orders(heights):
#     answer = [0] * len(heights)
#
#     for i in range(len(heights)-1, 0, -1):
#         for j in range(i-1, -1, -1):
#                 if heights[i] <= heights[j]:
#                     answer[i] = j + 1
#                     break # 불필요한 반복문 실행 제거
#
#     return  answer

## 스택 자료구조를 활용
def get_receiver_top_orders(heights):
    answer = [0] * len(heights)

    while heights: # 해당 stack이 비어있지 않으면 계속 반복해라
        height = heights.pop() # 4
        #            0  1  2  3
        # heights = [6, 9, 5, 7]

        #            0  1  2
        # heights = [6, 9, 5]

        #            0  1
        # heights = [6, 9]

        #            0
        # heights = [6]
        for i in range(len(heights)-1, -1, -1):
            if height <= heights[i]:
                answer[len(heights)] = i + 1
                break

    return  answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!

print("정답 = [0, 0, 2, 2, 4] / 현재 풀이 값 = ",get_receiver_top_orders([6,9,5,7,4]))
print("정답 = [0, 0, 0, 3, 3, 3, 6] / 현재 풀이 값 = ",get_receiver_top_orders([3,9,9,3,5,7,2]))
print("정답 = [0, 0, 2, 0, 0, 5, 6] / 현재 풀이 값 = ",get_receiver_top_orders([1,5,3,6,7,6,5]))