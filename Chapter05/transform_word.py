

origin_word = 'algorithm'
goal_word = 'alligator'
operation = []

def transform_word(origin_word, goal_word, cost):
    if len(goal_word) == 0:

        for ch in origin_word:
            cost += 20
        operation.append(cost)
        return True
    elif len(origin_word) == 0:
        for ch in goal_word:
            cost += 20
        operation.append(cost)
        return True
    else:
        if origin_word[0] == goal_word[0]:
            cost += 5
            transform_word(origin_word[1:], goal_word[1:], cost)
        else:
            cost += 20
            transform_word(origin_word, goal_word[1:], cost) or transform_word(origin_word[1:], goal_word, cost)

# base case: 1. copy when the last chat is the same; 2. insert when the origin list is emptry; 3. delete when the origin list is larger
def dp_transform(origin_word, goal_word, cost):
    g_len = len(goal_word)
    o_len = len(origin_word)
    result_table = [ [0 for j in range(g_len + 1)] for i in range( o_len + 1 ) ]

    for i in range(o_len+1):
        for j in range(g_len+1):

            if i == 0:
                result_table[i][j] = j * 20
            elif j == 0:
                result_table[i][j] = i * 20
            elif origin_word[i-1] == goal_word[j-1]:
                # copy
                result_table[i][j] = result_table[i-1][j-1] + 5
            else:
                # [i][j-1], insert
                # [i-1][j], delete
                result_table[i][j] = 20 + min(result_table[i][j-1], result_table[i-1][j])

    return result_table

transform_word(origin_word, goal_word, 0)
print( min(operation) )

print("\n".join( map(str, dp_transform(origin_word, goal_word, 0) ) ) )
