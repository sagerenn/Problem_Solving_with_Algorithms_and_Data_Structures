import random
from insertion_sort import insert_sort_2

def quick_sort(num_list, start, end):

    # when the length of list is greater than one
    if end - start > 0:

        # use the start item as the pivot
        pivot = start

        # compare between the start and the end
        left_mark = start + 1
        right_mark = end

        # the right side is larger then pivot, otherwise, the left is less
        # move the mark to converging on the split point
        # the left mark increase or the right mark decrement will eliminate the loop  
        while right_mark > left_mark:

            # when reach the left or right item are out of place, exchange them
            if num_list[right_mark] < num_list[pivot] and num_list[pivot] < num_list[left_mark]:
                num_list[left_mark], num_list[right_mark] = num_list[right_mark], num_list[left_mark]
                left_mark += 1
                right_mark -= 1
            else:
                # must include the equal to avoid there are three same item in the list and the mark stop 
                if num_list[left_mark] <= num_list[pivot]:
                    left_mark += 1
                if num_list[right_mark] >= num_list[pivot]:
                    right_mark -= 1

        # after the loop, the left and right mark will be on the split point or the next of the split point(the left increase)
        if num_list[pivot] >= num_list[right_mark]:
            num_list[pivot], num_list[right_mark] = num_list[right_mark], num_list[pivot]
            split_point = right_mark
        else:
            num_list[pivot], num_list[right_mark-1] = num_list[right_mark-1], num_list[pivot]
            split_point = right_mark - 1

        quick_sort(num_list, start, split_point-1)
        quick_sort(num_list, split_point+1, end)


def qsort(num_list, start, end):

    if end > start:

        median_three = [start, end, (start + end)//2]
        min_value = min([ num_list[start], num_list[end], num_list[(start + end)//2] ])
        max_value = max([ num_list[start], num_list[end], num_list[(start + end)//2] ])
        for i in range(3):
            if num_list[median_three[i]] >= min_value and num_list[median_three[i]] <= max_value:
                pivot = median_three[i]
                num_list[end], num_list[pivot] = num_list[pivot], num_list[end]
                break
        pivot = end
        left_mark = start
        right_mark = end - 1

        while True:

            # unstable
            while num_list[left_mark] <= num_list[pivot] and right_mark >= left_mark:
                left_mark += 1
                
            while num_list[right_mark] >= num_list[pivot] and right_mark >= left_mark:
                right_mark -= 1

            if right_mark < left_mark:
                break
            else:
                num_list[left_mark], num_list[right_mark] = num_list[right_mark], num_list[left_mark]
                left_mark += 1
                right_mark += 1

        num_list[left_mark], num_list[pivot] = num_list[pivot], num_list[left_mark]
        split_point = left_mark
        qsort(num_list, start, split_point-1)
        qsort(num_list, split_point+1, end)


def qsort_insert(num_list, part_limit):
    if part_limit >= len(num_list):
        insert_sort_2(num_list)
    else:
        qsort(num_list, 0, len(num_list)-1)


if __name__ == "__main__":
    count = 0
    test_list = [random.randint(1, 1000000) for i in range(2000)]
    quick_sort(test_list, 0, len(test_list) - 1)
    print(test_list, count)

    count = 0
    # test_list = [54,26,93,17,77,31,44,55,20]
    test_list = [random.randint(1, 1000000) for i in range(2000)]
    qsort(test_list, 0, len(test_list) - 1)
    print(test_list, count)

    # test_list = ['P','Y','T','H','O','N']
    # qsort(test_list, 0, len(test_list) - 1)
    # print(test_list)

