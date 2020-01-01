

def insert_sort(num_list):

    # the item need to insert bask to the sorted sublists
    for i in range(1, len(num_list)):

        # each pass the item need to insert back to the sub-ordered list
        temp = num_list[i]

        # the previous one of the each pass item
        j = i - 1


        while j >= 0:
            if num_list[j] > temp:
                num_list[j+1] = num_list[j]
                j -= 1
            else:
                break
        if j == -1:
            num_list[0] = temp
        else:
            num_list[j+1] = temp

    return num_list


def insert_sort_2(num_list):

    for i in range(1, len(num_list)):
        current_value = num_list[i]
        position = i

        # comparing with the previous value, if larger, change to current value and current postion move to previous
        # position must be larger than 0
        while position > 0 and num_list[position - 1] > current_value:
            num_list[position] = num_list[position - 1]
            position -= 1
        # stay on the position , right to less, left to larger
        num_list[position] = current_value

    return num_list


def insert_sort_3(num_list):
    # start from the second end, assumpt the last item is sorted alone
    i = len(num_list) - 2

    while i >= 0:

        # the current item need to insert to the right side of ordered subset list
        position = i
        current_value = num_list[position]

        # the currect item need to insert to ordered list is whether in the range of the (position+1, len(num_list)-2)
        # if the next right ordered item is larger than the current value, shift to left
        while position < len(num_list) - 1 and num_list[position + 1] > current_value:
            # shifting
            num_list[position] = num_list[position + 1]
            position += 1
        
        num_list[position] = current_value
        i -= 1
    return num_list

test_list = [34,5,6,56,7,34,5,4]
print(insert_sort(test_list))
test_list = [34,5,6,56,7,34,5,4]

print(insert_sort_2(test_list))
# test_list = [34,5,6,56,7,34,5,4]

print(insert_sort_3(test_list))