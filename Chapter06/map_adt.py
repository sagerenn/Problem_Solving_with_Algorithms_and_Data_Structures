
# there is limit size of every object, but the dictonary of python is not.
# when the hash table is full, the new item will replace the old one.
class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.list_size = 0

    def check_prime(self, num):
        prime = True
        for i in range(2, prime//2 + 2):
            if prime % i == 0:
                prime = False
                break
        return prime

    def get_prime(self, num, time=2):
        start = int(num*time) + 1
        while not self.check_prime(start):
            start += 1
        return start

    def rehash_func(self, hash_value, i):
        return (hash_value + i**2) % self.size # the hash_value can be replaced to hash_value

    def rehash_all(self):
        slots = self.slots.copy()
        data = self.data.copy()
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.list_size = 0
        for i in range(len(slots)):
            self.put(slots[i], data[i])


    def hash_func(self, key):
        slot = key % self.size
        if self.slots[slot] != None and self.slots[slot] != key:
            i = 1
            temp = self.rehash_func(slot, i)

            # meet the same key or the empty slot, back to the origin slot is the base case
            while self.slots[temp] != key and self.slots[temp] != self.slots[slot] and self.slots[temp] != None:
                i += 1
                temp = self.rehash_func(temp, i)
            return temp
        else:
            return slot

    def put(self, key, value):
        if self.size == self.list_size:
            self.size = self.get_prime(self.size)
            self.rehash_all()
        slot = self.hash_func(key)
        if self.slots[slot] != key:
            self.list_size += 1

        self.slots[slot] = key
        self.data[slot] = value

    def get(self, key):
        slot = self.hash_func(key)

        # avoid the condition of full list and return the origin slot
        if self.slots[slot] == key:
            return self.data[slot]
        else:
            return None

    def get_table_size(self):
        return self.size

    def __len__(self):
        return self.list_size

    def __delitem__(self, key):
        slot = self.hash_func(key)
        if self.slots[slot] == key:
            self.slots[slot] = None
            self.data[slot] = None
            self.list_size -= 1
            return True
        else:
            return False

    def __contains__(self, key):
        slot = self.hash_func(key)
        if self.slots[slot] == key:
            return True
        else:
            return False

    def keys(self):
        return self.slots

    def values(self):
        return self.data

    __getitem__ = get
    __setitem__ = put


if __name__ == "__main__":
    ht = HashTable()
    for i in range(11):
        ht[i] = i**2
    print(ht.keys(), ht.values(), sep='\n')

    ht[45] = 'erg'
    ht.put(57, 'ergth')
    print(ht.keys(), ht.values(), len(ht), 45 in ht, 567 in ht, sep='\n')
    print(ht[57], ht.get(67), sep='\n')
    ht[45] = '23er2'
    ht[24] = '3g345h'
    print(ht.keys(), ht.values(), len(ht), ht.get_table_size(), sep='\n')

