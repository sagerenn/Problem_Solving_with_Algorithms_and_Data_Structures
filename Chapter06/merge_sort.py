

def merge_sort(num_list):
    print("Splitting" , num_list)
    if len(num_list) > 1:
        # make the pieces of which length is not more than one on the left firstly or each sublist has ordered
        mid = len(num_list)//2
        left = num_list[:mid]
        right = num_list[mid:]
        merge_sort(left)
        merge_sort(right)

        left_index = 0
        right_index = 0
        parent_index = 0

        # in the parent call stack, the left and right sublist have sorted, compare both of them at the same time starting at 0,
        # the smaller one will save to the parent list(the item have splited to the sublist, the info of parent can be overwrited.) and move forward
        # to get out of one sublist and the other one will remain the most larger items
        while left_index < len(left) and right_index < len(right):
            if left[left_index] > right[right_index]:
                num_list[parent_index] = right[right_index]
                right_index += 1
            # lefthalf[i] <= righthalf[j] ensures that the algorithm is stable. 
            else:
                num_list[parent_index] = left[left_index]
                left_index += 1
            parent_index += 1

        # check the left sublist whether is empty
        while left_index < len(left):
            num_list[parent_index] = left[left_index]
            left_index += 1
            parent_index += 1

        # check the right sublist whether is empty
        while right_index < len(right):
            num_list[parent_index] = right[right_index]
            right_index += 1
            parent_index += 1
    print("Merge" , num_list)


test_list = [34,5,6,56,7,34,4]
merge_sort(test_list)
print(test_list)
