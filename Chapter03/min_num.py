import random
import time

def min_num1(num_list):
    if len(num_list) == 0:
        return None
    min = num_list[0]
    for i in num_list:
        if i < min:
            min = i
    return min

# the min item must be less than all items of list
def min_num2(num_list):
    for i in num_list:
        count = 0
        for j in num_list:
            if i > j:
                count += 1
        if count == 0:
            return i

    
test_list = [random.randint(-1000,10000) for i in range(10000)]

start_time = time.time()
a = min_num1(test_list)
end_time = time.time()

print(a, end_time - start_time)

start_time = time.time()
b = min_num2(test_list)
end_time = time.time()

print(b, end_time - start_time)
