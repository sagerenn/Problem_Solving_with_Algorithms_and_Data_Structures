
# O(2^n)
def rec_sack(item_list, knapsack_size):
    if knapsack_size <= 0 or len(item_list) <= 0:
        return 0
    else:
        max = 0
        for i in range(len(item_list)):
            if item_list[i][1] <= knapsack_size:
                a = item_list[i][2] + rec_sack( item_list[i+1:] + item_list[0:i], knapsack_size-item_list[i][1] )
                if max < a:
                    max = a
        return max

# def rec_sack_memo(item_list, knapsack_size):
    


# 1. the item can/can't be duplicated
# 2. the weight of item can be same
# 3. 
def dp_sack(item_list, knapsack_size):
    hash_table = [None] * ( knapsack_size + 1 )
    max_table = [0] * ( knapsack_size + 1 )

    for i in range(knapsack_size + 1):
        for j in item_list:
            if i - j[1] == 0:
                if hash_table[i] == None or max_table[i] < j[2]:
                    hash_table[i] = [j]
                    max_table[i] = j[2]
            elif i - j[1] > 0:
                # temp = i - j[1]
                # duplicated = False
                # while hash_table[temp] != None and temp > 0:
                #     if j == hash_table[temp]:
                #         duplicated = True
                #         break
                #     temp -= hash_table[temp][1]
                # if duplicated:
                #     continue


                # compare with the previous that less than 1 kg
                if max_table[i-1] > j[2] + max_table[i - j[1]] and max_table[i-1] > max_table[i]:
                    if j in hash_table[i-1]:
                        continue
                    max_table[i] = max_table[i-1] 
                    hash_table[i] = hash_table[i-1].copy()
                elif max_table[i] < j[2] + max_table[i - j[1]]:
                    if hash_table[ i - j[1] ] and j in hash_table[ i - j[1] ]:
                        continue
                    max_table[i] = j[2] + max_table[i - j[1]]
                    # keep track the item in the specific weight to avoid repeatly selecting
                    if hash_table[ i - j[1] ]:
                        hash_table[i] = hash_table[ i - j[1] ].copy()
                    else:
                        hash_table[i] = []
                    hash_table[i].append( j )

    # t_size = knapsack_size
    # result = []
    # while hash_table[t_size] != None and t_size - hash_table[t_size][1] >= 0:
    #     result.append(hash_table[t_size])
    #     t_size -= hash_table[t_size][1]

    # return result
    return hash_table[knapsack_size]

# max(f(w)) = any(v(i,w(i))) + max(f(w-w(i)))
# the max value is depend on the weight limit and the items(only selected once)
# the max value need to compare the the weight less one with the combination of any(v(i,w(i))) + max(f(w-w(i))) because the weights of items is not continuous.
# e.g. with three items to get the max value with 4kg has been known, how about the four items with 5kg, and new item is 1kg?
# It's not about the order of the item appeared. but the intermedia result is not the max value of all items given in the beginning. it's just the max value of subset of items.

# if the value has two factors, we need to build a two dimension table to solve the problem.
def dp_sack_2(item_list, knapsack_size):

    K = [[0 for w in range(knapsack_size + 1)] for i in range(len(item_list)+1)]

    # Recurrence
    for item_num in range(1, len(item_list)+1):
        for limit_weight in range(1, knapsack_size + 1):
            item_weight = item_list[item_num-1][1]
            item_value = item_list[item_num-1][2]

            # if item weight is larger than the limit weight, it means the item cannot be used to fill the knapsack and we have to use the previous items to fill in, so it will be K[item_num-1][limit_weight].
            if item_weight > limit_weight:
                K[item_num][limit_weight] = K[item_num-1][limit_weight]
            else:
                # don't need to compare with the condition of the weight less then one, because if the base case, only one or two item, the limit weight larger, the value is not least than the less limit weight. 
                K[item_num][limit_weight] = max(K[item_num-1][limit_weight], K[item_num-1][limit_weight-item_weight] + item_value)

    i = len(item_list)
    w = knapsack_size
    result = []
    while K[i][w] != 0:
        # need to check the max value whether inherit from the subset of items
        if K[i][w] != K[i-1][w]:
            result.append(item_list[i-1])
            w -= item_list[i-1][1]
        i = i-1
        
    return result

knapsack_size = 20

item_list = [
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 8],
    [4, 5, 8],
    [5, 9, 10],
]

print( rec_sack(item_list, knapsack_size) )
print( "\n".join(map(str, dp_sack(item_list, knapsack_size))) )
print()
print()
print()
print()
print( "\n".join(map(str, dp_sack_2(item_list, knapsack_size))) )
