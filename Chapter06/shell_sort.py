
def insert_sort(num_list, start, gap):
    # the loop index to record the item which need to order
    position = start + gap

    # the unordered item must be in the range of origin list
    while position < len(num_list):

        # keep the unordered item to compare back to the left ordered sublist
        current_value = num_list[position]
        current_position = position

        # the unordered item is less then the left one
        while current_position > start and num_list[current_position-gap] > current_value:

            # move the left one to the right
            num_list[current_position] = num_list[current_position-gap]

            # keep to compare with the further left item
            current_position -= gap

        # when the item reach to the start or the place where the left part is smaller than the unordered item, put it into the place
        num_list[current_position] = current_value

        # move forward to the remaining item on the right side
        position += gap

def shell_sort(num_list, gap):
    # for larger list, the gap may be reduced by divide 2, to make the item closer to the final location.(4>2>1)
    # gap = 3

    while gap > 0:
        # for each sublist
        for i in range(gap):
            # do the insertion sort
            insert_sort(num_list, i, gap)
        gap = gap // 2
        
    # finally, move the remain unordered item
    # insert_sort(num_list, 0, 1)
    
    return num_list

if __name__ == "__main__":
    test_list = [54,26,93,17,77,31,44,55,20]
    print(shell_sort(test_list, 4))

