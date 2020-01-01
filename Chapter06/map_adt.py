
# there is limit size of every object, but the dictonary of python is not.
# when the hash table is full, the new item will replace the old one.
class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.list_size = 0

    def rehash_func(self, hash_value):
        return (hash_value + 1) % self.size # the hash_value can be replaced to hash_value

    def hash_func(self, key):
        slot = key % self.size
        if self.slots[slot] != None and self.slots[slot] != key:
            temp = self.rehash_func(slot)

            # meet the same key or the empty slot, back to the origin slot is the base case
            while self.slots[temp] != key and self.slots[temp] != self.slots[slot] and self.slots[temp] != None:
                temp = self.rehash_func(temp)
            return temp
        else:
            return slot

    def put(self, key, value):
        slot = self.hash_func(key)
        self.slots[slot] = key
        self.data[slot] = value
        self.list_size += 1


    def get(self, key):
        slot = self.hash_func(key)

        # avoid the condition of full list and return the origin slot
        if self.slots[slot] == key:
            return self.data[slot]
        else:
            return None

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
    print(ht.keys(), ht.values(), sep='\n')

