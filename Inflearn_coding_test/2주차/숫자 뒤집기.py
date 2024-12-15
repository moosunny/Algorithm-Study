input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 이 부분을 채워보세요!
    one_cnt = 0
    zero_cnt = 0

    if string[0] == "0":
        one_cnt += 1
    if string[0] == "1":
        zero_cnt += 1
    for i in range(len(string) -1):
        if string[i] != string[i+1]:
            if string[i+1] == "0":
                one_cnt +=1
            elif string[i+1] == "1":
                zero_cnt += 1
    return min(zero_cnt, one_cnt)

result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)