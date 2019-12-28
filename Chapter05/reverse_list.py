
def ite_reverse(test_list):
    result_list = []
    while test_list:
        result_list.append( test_list.pop() )
    return result_list

def rec_reverse(test_list):
    if not test_list:
        return []
    else:
        return [test_list.pop()] + rec_reverse(test_list)

# inline exchange
def rec_reverse_2(test_list, start=0, end=-1):
    if end == -1:
        end = len(test_list) - 1
    if end <= start:
        return
    else:
        test_list[start], test_list[end] = test_list[end], test_list[start]
        rec_reverse_2(test_list, start+1, end-1)
        return test_list


print(ite_reverse([4,67,5,3,5,8]))
print(rec_reverse([4,67,5,3,5,8]))
print(rec_reverse_2([4,67,5,3,5,8]))
print(rec_reverse_2([4,67,9,5,8]))