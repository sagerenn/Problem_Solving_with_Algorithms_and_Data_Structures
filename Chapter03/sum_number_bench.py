import time 

def sum1(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum

def sum2(n):
    return (1+n)*n/2

start_time = time.time()
a = sum1(10000000)
end_time = time.time()

print(a, end_time - start_time)

start_time = time.time()
b = sum2(1000000000)
end_time = time.time()

print('{0:.0f}'.format(b), end_time - start_time)
