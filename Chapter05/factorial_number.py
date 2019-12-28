def itera_factorial(num):
    result = 1
    while num >= 1:
        result *= num
        num -= 1
    return result

def rec_factorial(num):
    if num == 1:
        return 1
    else:
        return num * rec_factorial(num-1)


print(itera_factorial(5))
print(rec_factorial(5))