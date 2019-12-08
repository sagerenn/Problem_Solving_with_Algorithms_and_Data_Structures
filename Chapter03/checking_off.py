
# pass a list to function, change the value of list will effect on the origin one

def anagram_check(s1, s2):
    if len(s1) != len(s2):
        return False

    list_s1 = list(s1)
    list_s2 = list(s2)

    # n^2/2 + n/2
    for i in range(len(list_s1)):
        for j in range(len(list_s2)):
            if list_s1[i] == list_s2[j]:
                list_s1[i], list_s2[j] = None, None
    
    for k in range(len(list_s1)):
        if list_s1[k] != None or list_s2[k] != None:
            return False

    return True


# sort and compare bt index
def sort_check(s1, s2):

    if len(s1) != len(s2):
        return False
    list_s1 = list(s1)
    list_s2 = list(s2)

    # the execution time depends on the sort algorithm
    # common n log n, or n^2
    list_s1.sort()
    list_s2.sort()

    for i in range(len(list_s1)):
        if list_s1[i] != list_s2[i]:
            return False

    return True



def brute_force(s1, s2):

    def permute(a, l, r): 
        if l==r: 
            if a == s2:
                return True
        else: 
            for i in range(l,r+1): 
                a[l], a[i] = a[i], a[l] 
                permute(a, l+1, r) 
                a[l], a[i] = a[i], a[l] # backtrack 

    if len(s1) != len(s2):
        return False

    list_s1 = list(s1)
    permute(list_s1, 0, len(list_s1)-1)
    return False

# O(n+r)
def count_table(s1, s2):
    if len(s1) != len(s2):
        return False
    
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        c1[ ord(s1[i]) - ord('a') ] += 1

    for i in range(len(s2)):
        c2[ ord(s2[i]) - ord('a') ] += 1

    for i in range(len(c1)):
        if c1[i] != c2[i]:
            return False
    return True

print(anagram_check("weffrg", "eefrgw"))
print(anagram_check("wefrg", "efrgw"))
print(sort_check("weffrg", "eefrgw"))
print(sort_check("wefrg", "efrgw"))
print(count_table("weffrg", "eefrgw"))
print(count_table("wefrg", "efrgw"))
