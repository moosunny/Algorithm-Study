numbers = [1, 1, 1, 1, 1]
target_number = 3



def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    # 구현해보세요!
    all_ways = []



    def get_all_ways_by_doing_plus_or_minus(array, current_index, current_sum):
        if current_index == len(array):
            all_ways.append(current_sum)
            return
        print(current_index, current_sum)
        get_all_ways_by_doing_plus_or_minus(array, current_index + 1, current_sum + array[current_index])
        get_all_ways_by_doing_plus_or_minus(array, current_index + 1, current_sum - array[current_index])

    get_all_ways_by_doing_plus_or_minus(array, 0, 0)

    target_count = 0

    for way in all_ways:
        if target == way:
            target_count += 1

    return target_count

print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!