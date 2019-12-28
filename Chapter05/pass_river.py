
temp = []

# use the result var to record, no the middle var, because each recursive call will change the initial value to the base case, if the step is false, you need to restore it. That is complex.
# using memoization need to figure out the changable var and keep track of them

# why change the order move items from side to side, the goal can be achiaved?
def over_river(a, b, c, d, f):
    if [a, b] == [3, 3]:
        print([d, f], [a, b])
        return True
    elif d < 0 or f < 0 or a < 0 or b < 0:
        return False
    elif [a, b, c] in temp:
        return False
    elif (b > a and a > 0) or ( f > d and d > 0 ):
        return False
    else:
        print([d, f], [a, b])
        temp.append([a, b, c])

        if c == 1:
            return over_river(a,b-1,-1,d,f+1) or \
                over_river(a-1,b,-1,d+1,f) or \
                over_river(a-1,b-1,-1,d+1,f+1) # no the only one people can be returned
        else:
            return over_river(a+2,b+0,1,d-2,f) or \
            over_river(a+0,b+2,1,d,f-2) or \
            over_river(a+1,b+1,1,d-1,f-1)


over_river(0, 0, -1, 3, 3)
