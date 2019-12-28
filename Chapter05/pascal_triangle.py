import math 

# def format_triangle(num_list, rows):

# O(n^3)
def iter_triangle(rows):
    for i in range(rows):
        # temp = []
        for j in range(i+1):
            print(math.factorial(i) / (math.factorial(j) * math.factorial(i-j)), end=" ")
            # temp.append(math.factorial(i) / (math.factorial(j) * math.factorial(i-j)), rows)
        print()

# O(n^2)
def iter_triangle_2(rows):
    temp = [ [None]*rows for i in range(rows)]
    for i in range(rows):
        for j in range(i+1):

            if i == 0 :
                temp[i][j] = 1
            else:
                if j <= 0 or j >= i:
                    temp[i][j] = 1
                else:
                    temp[i][j] = temp[i-1][j-1] + temp[i-1][j]

    for i in temp:
        for j in i:
            if j != None:
                print(j, end=" ")
        print()



iter_triangle(4)
print()
iter_triangle_2(5)