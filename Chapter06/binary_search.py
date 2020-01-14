
# status best avg worst
# in 1 O(logN) O(N)
# not in O(N) O(N) O(N)
def iter_bin_search(num_list, goal):
    count = 0

    # the question is find the item in the list, we need to find the item in the subset of list, so it's neseccery to remember the start and the end to arrange the list.
    start = 0
    end = len(num_list) - 1
    middle = (start + end) // 2

    while num_list[middle] != goal:
        count += 1
        if start >= end:
            return False, count
        elif num_list[middle] < goal:
            start = middle + 1
        else:
            end = middle - 1
        middle = (start + end) // 2

    return middle, count

# the recursive call will cost two times than the iteration call, as it need to create sub-function and return the value
def rec_bin_search(num_list, goal, start, end, count):
    count += 1
    middle = (start + end) // 2

    if num_list[middle] != goal:
        if end <= start:
            return False, count
        elif num_list[middle] < goal:
            return rec_bin_search( num_list, goal, middle+1, end, count )
        else:
            return rec_bin_search( num_list, goal, start, middle-1, count )

    else:
        return middle, count


# test_list = [2,4,7,9,23,53,76,94,1234,6787]
# test_goal = 76
# print( iter_bin_search(test_list, test_goal) ) 
# print( rec_bin_search(test_list, test_goal, 0, len(test_list), 0) ) 

