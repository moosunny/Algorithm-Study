shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]

def binary_search(array, target):

    min_index = 0
    max_index = len(array) - 1
    guess_index = (min_index + max_index)//2

    while min_index <= max_index:
        if array[guess_index] == target:
            return True
        elif array[guess_index] > target:
            max_index = guess_index - 1
        else:
            min_index = guess_index + 1
        guess_index  = (min_index + max_index) // 2

    return False

def is_available_to_order(menus, orders):
    # 이 부분을 채워보세요!
    menus.sort()

    for order in orders:
        if not binary_search(menus, order):
            return False
    return True

    # order_cnt = len(orders)
    #
    # for customer in orders:
    #     for food in menus:
    #         if customer == food:
    #             # print("YES")
    #             order_cnt -= 1
    # if order_cnt != 0:
    #     return False
    # return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)