

def select_sort(num_list):
    pass_num = len(num_list) - 1
    while pass_num > 0:

        # remember the larger value need to exchange
        max_position = pass_num
        for i in range(pass_num):
            if num_list[i] > num_list[max_position]:
                max_position = i
        # do the exchange after one pass
        num_list[max_position], num_list[pass_num] = num_list[pass_num], num_list[max_position]
        pass_num -= 1

    return num_list


test_list = [34,5,6,56,7,34,5,4]
print(select_sort(test_list))