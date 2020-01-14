

def right_large_bubble(num_list):
    # need to compare the n-1 time, to find the n-1 larger item and remain 1
    count = 0
    for pass_num in range(1, len(num_list)):

        # each pass, the range of comparisom will be smaller
        for j in range(len(num_list)-pass_num):
            count += 1

            if num_list[j] > num_list[j+1]:
                # swap, simultaneous
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

    return num_list, count

def left_large_bubble(num_list):
    count = 0
    # first need to compare n-1 pairs of item, step by step to 0 pair
    for pass_num in range(len(num_list)-1, 0, -1):

        for i in range(pass_num):
            count += 1
            if num_list[i] < num_list[i+1]:
                temp = num_list[i]
                num_list[i] = num_list[i+1]
                num_list[i+1] = temp
    return num_list, count

# if there is no exchange, the list is ordered.
def shot_bubble(num_list):
    count = 0
    exchange = True
    pass_num = len(num_list) - 1
    while pass_num > 0 and exchange:
        exchange = False
        for i in range(pass_num):
            count += 1
            if num_list[i] > num_list[i+1]:
                exchange= True
                num_list[i+1], num_list[i] = num_list[i], num_list[i+1]
        pass_num -= 1
    return num_list, count

def bidirect_bubble(num_list):
    direct = 'right'
    exchange = True
    start = 0
    end = len(num_list) - 1
    temp = 0
    while end > start and exchange:
        exchange = False
        if direct == 'right':
            while temp < end:
                if num_list[temp+1] < num_list[temp]:
                    num_list[temp+1], num_list[temp] = num_list[temp], num_list[temp+1]
                    exchange = True
                temp += 1
            direct = 'left'
            end -= 1
        else:
            while temp > start:
                if num_list[temp-1] > num_list[temp]:
                    num_list[temp-1], num_list[temp] = num_list[temp], num_list[temp-1]
                    exchange = True
                temp -= 1
            direct = 'right'
            start += 1

    return num_list

if __name__ == "__main__":
    test_list = [34,5,6,56,7,34,5,4]
    print(right_large_bubble(test_list))
    test_list = [34,5,6,56,7,34,5,4]
    print(left_large_bubble(test_list))

    test_list = [34,5,6,56,7,34,5,4]
    print(shot_bubble(test_list))
    test_list = [34,5,6,56,7,34,5,4]
    print(bidirect_bubble(test_list))
    print()
    print()
    print()
    test_list = [20,30,40,90,50,60,70,80,100,110]
    print(right_large_bubble(test_list))
    test_list = [20,30,40,90,50,60,70,80,100,110]
    print(left_large_bubble(test_list))
    test_list = [20,30,40,90,50,60,70,80,100,110]
    print(shot_bubble(test_list))
    test_list = [20,30,40,90,50,60,70,80,100,110]
    print(bidirect_bubble(test_list))