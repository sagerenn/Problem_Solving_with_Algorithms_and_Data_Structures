from queue_adt import Queue


# O((n+b) * logb(k))
def radix_sort(num_list, base):
    digit_bins = [ Queue() for i in range(base) ]
    main_bin = Queue()
    max_length = 0
    for num in num_list:
        main_bin.enqueue(num)
        if len(str(num)) > max_length:
            max_length = len(str(num))

    for i in range(max_length):
        while not main_bin.is_empty():
            a = main_bin.dequeue()
            if i+1 > len(str(a)):
                index = 0
            else:
                index = int(str(a)[-1-i])
            digit_bins[index].enqueue(a)
        for q in digit_bins:
            while not q.is_empty():
                main_bin.enqueue( q.dequeue() )
    return main_bin

print( radix_sort([456,54,6,7,34,34,4,35,0,64,75,324,25,23,24,33,17,9,100], 10) )