
# generate the data
test_data = []
a = [0, 1]
for i in a:
    for j in a:
        for k in a:
            for m in a:
                test_data.append([i,j,k,m])


# logic gateway
for test in test_data:
    next_text = []
    final_test = 0
    if test[0] and test[1]:
        next_text.append(1)
    else:
        next_text.append(0)

    if test[2] and test[3]:
        next_text.append(1)
    else:
        next_text.append(0)
    
    if next_text[0] or next_text[1]:
        final_test = 1
    else:
        final_test = 0

    if final_test:
        final_test = 0
    else:
        final_test = 1

    print(test, final_test)


# 1/4 + 1/4 - (1/4)^2