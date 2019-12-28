import random
# list all possible ordered solution, need to remove duplicated
def money_combination(money, arsenal):

    # save the current solution line by line
    result = []
    temp_result = {}
    # all kinds of arsenal can sovle the problems
    for i in arsenal:

        # reduce the money to base case
        if money - i >= 0:

            # get the all result from the less money
            count.append(0)
            previous_result = money_combination(money - i, arsenal)
            temp_result[money - i] = previous_result
            # if the less money result is exist , append the current money to each solution
            if previous_result:
                for line in previous_result:
                    line.append(i)
                    result.append(line)

            # if not, it means the step will be the base case, and it make the money to zero
            else:
                result.append([i])

    # return the all solution
    return result

# in recursion, we need a variable to track all call and save some data, we need to define the var outsite the recursion, and pass it.
def min_money_combine(money, arsenal, temp_result):
    min_num = money
    if money in arsenal:
        temp_result[money] = 1
        return 1
    elif temp_result.get(money):
        return temp_result.get(money)
    else:
        for i in [ j for j in arsenal if money-j>=0 ]:
            count.append(0)

            num = 1 + min_money_combine(money-i, arsenal, temp_result)
            if num < min_num:
                min_num = num
        temp_result[money] = min_num
    return min_num


def dp_money_change(money, arsenal):
    min_list = []
    for i in range(money+1):
        min_i = i
        for j in [k for k in arsenal if k<=i]:
            count_2.append(0)
            if min_list[ i - j ] + 1 < min_i:
                min_i = min_list[ i - j ] + 1

        min_list.append(min_i)

    return min_list[money]


def dp_money_change_2(money, arsenal):
    min_list = [0] * (money+1)
    min_value_list = [0] * (money+1)
    for i in range(money+1):
        min_i = i
        temp = 0
        for j in [k for k in arsenal if k<=i]:
            count_2.append(0)
            if min_list[ i - j ] + 1 <= min_i:
                # when get the min count, save the count num and corresponding coins
                min_i = min_list[ i - j ] + 1
                temp = j
        min_list[i] = min_i
        min_value_list[i] = temp
    num_list = []
    while money != 0:
        num_list.append(min_value_list[money])
        money -= min_value_list[money]
    return num_list

count = []
count_2 = []
temp_result = {}
# temp = money_combination(35, [25,10,5,1])
# for i in range(10):
#     print(temp[ random.randrange(0,len(temp)) ])


print(min_money_combine(63, [25,21,10,5,1], temp_result))
print(len(count))

print(dp_money_change(63, [25,21,10,5,1]))
print(len(count_2))


print(dp_money_change_2(63, [25,21,10,5,1]))
print(dp_money_change_2(33, [25,8,10,5,1]))
