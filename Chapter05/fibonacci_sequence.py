# O(2^n)
def rec_fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        a = rec_fibonacci(num-1)
        b = rec_fibonacci(num-2)
        return a + b

# O(n)
def rec_fibonacci_memo(num, result_list):
    if num == 0:
        result_list[num] = 0
        return 0
    elif num == 1:
        result_list[num] = 1
        return 1
    else:
        if result_list[num-1]:
            a = result_list[num-1]
        else:
            a = rec_fibonacci_memo(num-1, result_list)

        if result_list[num-2]:
            b = result_list[num-2]
        else:
            b = rec_fibonacci_memo(num-2, result_list)
        
        result_list[num] = a + b
        return result_list[num]

# O(n)
def dp_fibonacci(num):
    temp_list = [None] * num
    for i in range(num):
        if i > 1:
            temp_list[i] = temp_list[i-1] + temp_list[i-2]
        else:
            temp_list[i] = i 
    return temp_list[num-1], temp_list


def ite_fibonacci(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    elif num == 3:
        return 1
    else:
        for i in range(num):
            if i <= 2:
                n1 = 0
                n2 = 1
                n3 = 1
            else:
                n1 = n2
                n2 = n3
                n3 = n1 + n2
    return n3

result_list = [None]*10
print(rec_fibonacci_memo(len(result_list)-1, result_list), result_list)

print(dp_fibonacci(10))
print(ite_fibonacci(10))