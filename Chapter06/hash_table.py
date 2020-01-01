

def hashing(num_list):
    hash_table = [None for i in range(10)]
    for i in num_list:
        hash_table[ i%10 ] = i
    return hash_table

def hash_search(hash_table, goal):
    if hash_table[ goal % len(hash_table) ] == goal:
        return True
    else:
        return False

def hash_func_folding(num, table_size):
    temp = ''
    count = 0
    result = 0
    for ch in str(num):
        temp += ch
        count += 1
        if count == 2:
            result += int(temp)
            temp = ''
            count = 0
    if temp:
        result += int(temp)
    return result % table_size

def hash_func_square(num, table_size):
    num = int(str(num**2)[1:-1])
    return num % table_size

def hash_func_string(test_str, table_size):
    result = 0
    for i in range(len(test_str)):
        result += ord( test_str[i] ) * (i+1)
    return result % table_size

test_list = [34,5,7,8,23,679]
hash_list = hashing(test_list)
print( hash_search( hash_list, 235 ) )

print( hash_func_folding(3465674, 11) )
print( hash_func_square(66, 11) )
print( hash_func_string('cat', 11) )