
# statue best avg worst
# in: O(1) O(n/2) O(n)
# not: O(n) O(n) O(n)
def sequential_search(item_list, goal):
    count = 0

    for i in range( len(item_list) ):
        count += 1

        if goal == item_list[i]:
            return i

    return False, count

# statue best avg worst
# in: O(1) O(n/2) O(n)
# not: O(1) O(n/2) O(n)
def order_sequential_search(item_list, goal):
    count = 0
    for i in range( len(item_list) ):
        count += 1
        if goal == item_list[i]:
            return i
        elif goal < item_list[i]:
            return False, count

    return False, count


# print( sequential_search([45,6,23,56,5], 23)  )
# print( sequential_search([45,6,23,56,5], 2)  )
# print( order_sequential_search([1,3,4,5,6,23,55,67], 34)  )
# print( order_sequential_search([1,3,4,5,6,23,55,67], 23)  )

