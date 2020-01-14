# Searching

the algorithmic process to find an item in a collection of items, always retuen boolean value or the position

## Sequential search
When the items store in the linear data structure, the position of anyone will be relative to the others. We can visit them in sequence to find the goal.

to analyze the algorithm, we need to decide on a basic unit of computation. In searching, it makes sense to use the comparison times to check the performance.

## Binary Search
with the ordered list, we need to find to limit of goal number, we can start at the middle, and repeat until the number is found or the limit reach.

When we compare i time and the list only remain one(base case), the searching ends. i time remains: n/(2^i) = 1, i = log(n), so the time complexity is O(log N)

But to sort the list may be so expensive.(large list or sort once, and search many times)


## hashing
A hash table is a collection of items which are stored in such a way as to make it easy to find it later. We need to know more about where the items might be when we go to look for them in the collection.
1. using the remainder(denominator?) to index the value. slot == position, named by an integer value. It can make sure the item locate in the range of slot names.
hash function: item % table_size == slot (hash value), hash_table[slot] = item or h(item) = item % table_size

for the collection of list, using the hash function to figure out the slot of item, and insert the item to the hash table. When a goal number comes, we only do the same process to find the position of item in the hash table. and compare with the item that is already in the hash table, and finish the search.

each slot only contains one item will work. It wlll be collision to contain two item in a same slot. 

so the hash table at least has the same size of the collecion of items.

How to make sure any item will in a unique slot? (key, perfect hash function)?
a. increasing the size of the hash table. It's suitable for small list, but not the large one.
b. minimize the number of collisions. like nature, add more factor or convertion to the list and mix it, randomly retrieve the item to get the unique. And need to reduce the size of hash table.

(1) folding method: divide the collection to equal-size pieces and add together. go further, some folding method reverse every other piece before the addition. 34566 --> ( 34 + 56 + 6 ) % 11 = 8
(2) mid-square method: to get the value of square the item, and extract some portion of the resulting digits. 55^2 = 3025 --> 02 / 11 = 2
(3) string can convert to ordinal(ascii) number char by char and add together. to remedy the anagram situation, we can use the position of the character as a weight. (Because a string only has the char and position properties, we can design the different weighting scheme based on the position.)

The hash function must be efficient, the time complexity require to O(1) for following the purpose of hashing.


### collision resolution
1. linear probing to find the open addressing, start at the origin hash value that occur the collision, and move circularly to the next slot until find the empty slot or return to the origin position. Maybe we can skip the item with (1, 3, ...) steps. We must be sure the skip to cover all the slots in the list to find the possible opening slot. To fulfill the requirement, the table size must be the prime number. (table_size % skip_steps != 0)

There will be a problem, the order of insertion or the clustering. The early item that happen collision and move to find a open slot, but the after number will should be in the slot have to move again. And the collision number will group together. 

Maybe you can change the skip steps to disperse the group. It can be refer as the rehashing. rehash(pos) = (pos + skip) % table_size

while searching, we check the item of origin slot. If it match, return True, or do a sequential search starting at the origin one to find the item until another open slot or back to the origin slot. So if the more item is not located in the correct slot, the search will be not efficient.

2. quadratic probing, instead of skip constant value, we can skip the value by the successive square of 1, 2, 3, 4... or 
origin_slot += 1^2, (2^2, 3^2, ..., i^2), how to make sure the quadratic probing will pass through all the slot?(prime number of table size?)

3. chaining, each slot handle a reference to a collection of items, and allow many item witch the same hash value to the same position. when searching, we found the origin slot, and we need to search again(sequential, binary, hash) to find the final result. on average, the fewer items will locate in the same slot. So the method may be efficient.

The size of hash table is `50% full` is better to gain the performance and spend less space.

the time complexity of hash is related to the load factor (λ, 6/11). the λ is small means there are fewer collision. Otherwise, the collision will happen frequently. if the collision resolution is more difficult, requiring the more comparison to find the slot.
method avg successful unsuccessful
line_probing (1/2)*( 1 + 1/(1-λ) ) (1/2)*( 1 + (1/(1-λ))**2 ) ??
chaining 1+λ/2 λ ??

## Map
An collection data type stores the key-value pairs. The key is used to loop up the associated value. e.g. the number of book in the library
we can use the hash table for the key list, and compute the slot of the key, to find the associated value with the same position in the other list. (hash value --> key --> value)

It's so difficult to restore the origin ordered list with the collision solution since lots of value skip its slot. So the dictionary is unordered list in python. And while extending the table size, we just need read the values one by one in the small table size and rehash to the new larger table.

# Sorting

the operations that can be used to analyze a sorting process
1. comparisons, to find the order (the most common way to measure the sorting procedure)
2. the exchange, costly operation

## bubble sort
If there are n items in the list, the first step need to compare n-1 pairs of items to find the larger ot the smallest value, the second step need to compare n-2 pairs and so on. Finally, after n-1 steps, the n-1 th larger value has been found by 1 comparison and left the smallest one.

Time Complexity:
1+2+...+(n-2)+(n-1) = n(n-1)/2, O(n^2) comparisons.
The exchange:
bast = 0, for the ordered list
avg = n(n-1)/4, half of the worst base
worst = n(n-1)/2, each comparison will task an exchange

This is inefficient sorting since it must exchange items before the final location is known. In contrast of the counting sort, to record the final position of the item. 
If during a pass there are no exchanges, then we know that the list must be sorted and stop. This is short bubble.

## selection sort 

reduce the exchange cost of bubble sort, remember the max position of each pass comparing with the beginning or end of the remain list. After pass through the list, exchange once to make sure the larger value in the correct position.

Time Complexity:
1+2+...+(n-2)+(n-1) = n(n-1)/2, O(n^2) comparisons.
The exchange:
bast = 0, for the ordered list
avg = (n-1)/2, half of the worst base
worst = n-1, each pass will task an exchange

## insertion sort

the origin list can be treat as the ordered part and the unordered part, the ordered part beginning at the start or end item of the list, pass through the unordered list one by one, to insert back to the ordered list in a order position or the end side by shifting the ordered item.

Time Complexity:
worst = n^2 comparisons, reverse ordered list
best = n comparisons, ordered list
The shifting:
worst: n^2, each pass will shift all the ordered sublist
best = 0, ordered list

The shifting process will require a third of the processing work of an exchange since only one assignment is performed.

It's suitable for nearly ordered list with best time complexity or the small list with low overhead. And the insertion sort is stable.

## Shell sort
As we can see the performance of insertion sort is good in the ordered list, so if we can preset the ability of order of list and finally use insertion sort once again, we can improve the time complexity from O(n^2) --> O(n). 
The origin list we can break into a number of sublist. For each sublist, we do the insert sort, the origin list will be more ordered and closer to the where they actually belong. To the final standard insertion sort, the shifting opetaion has reduced.
There are two method to breaking:
1. split by a gap or increment, e.g. [4,5,76,7,4,34,3,5], gap = 3, [ [0], [3], [6]  ] = [4, 7, 3], the number of sublist will be same with the gap. Maybe the size of first sublist will be larger than the others. The gap will make the order of list more closer to its position. Midlle in midlle, less in left, more in right.
2. the contiguous items of group number, e.g. [4,5,76,7,4,34,3,5], group_num = 3, [ [0], [1], [2] ] = [ 4, 5, 76 ], the number of sublist will be (n//2)(+1).

The insertion sort can be see as the shell sort start at 0, and the increment is 1.

Time Complexity:
if the increment is 2^k-1(1, 3, 5...), a shell sort can perform at O(n^(3/2))

## merge sort
Using divide and conquer strategy, split to origin list to left sublist and right sublist. f(n) = f(l) + f(r) + operation(n/2). Continue to split list in half until there is one or zero item left that has ordered.(base case) 
Always split one side until the side of item reduce to one or zero and merge, return. Using three index to keep track of the left sublist, right sublist, and the parent sublist on invoking. Compare the ordered left and right sublist at the same time beginning at each start position. each comparison will put the smaller one to the parent list with the parent index, and move forward. After compare with both of sublists, one of the sublists will remain. Add the remaining item to the parent list to return the previous call.

The parent list have split and stored the items into the left and right sublists with different address, so when merging, the item of parent list can be lost. And the sublist will take the extra space.

merge sort is a stable sort, which maintains the order of duplicate item in the list and is preferred in most case. e.g. [ (Carol, A), (Dave, A), (Ken, A), (Alice, B), (Eric, B) ]. The stable sort is useful for sorting multiple times by different keys, and wish the order by (keyA > keyB)

Time Complexity:
The list will be split 2^i = n, i = log n time to make sure all the sublist is 1 or 0, for each split or level, there are n item and need to compare n times, so it's O(N log N)
Space Complexity:
The max space is to call the min list(0 or 1) from the origin list, it hava the level of log N, the sum of each level will be the sum of the Geometric progression. 1 + 2 + 4 + n/2 = 1*(1-2^(logN))/(1-2) = O(N). So the merge sort is not suitable for the large data sets.

## quick sort
As the merge sort, the quick sort also use the divide and conquer strategy. Instead of extra space to store the sublist, the quick sort tries to find a split point, the final position, of pivot by partition, comparing with the remaining list except the pivot item from the start and end by converging and exchanging the item of both side is out of place(left need to be less, right need to be more). After find the split point, exchange the position of pivot and the mark. Finally recursively call to sort the left and the right part.

The pivot value can be selected by the technique named median of three(start_inde, middle_index, end_inde), the middle value , to avoid the situation of uneven list. The pivot value is used to split the list.

Time Complexity:
for even list, there are log(N) times pass. for each time, the avg comparison is (n-1) to the pivot. O(N log N)
if the pivot always devide a uneven list in the worst case, e.g. ordered list, left sublist 0, right sublist n-1, the time Complexity O(n time * n comparisons).

## counting sort
the quick sort make the pivot to the final split point, so if we can record all the final position of items, it's easy the restore the ordered list from the relationship of the final position and the item. `For a small range` of item, we can initialize a list to store the item by index and the count of appear by value. after counting all the items, the result list of recording the final location can read from left to right, and return the number of item with the counting digit.

Time Complexity:
O(n + r)
Space Complexity:
O(r), the size of the list to recording

## radix sort
if the values of items spread wide range, we cannot use the counting sort to create a large list to index the item. But we can use ten stacks(0,1,2,3,...9) to store the items from ones place to tens place, each time push the items into the stacks by one digit, pop from the stacks to get more ordered list. The ones place is less significant to the thousands place, so after push by the most significant digit, the list will be sort.


Time Complexity:
O(n + r)
