# Mathew Thomas - #001346588

class HashTable:

    # Initiate our hash table with empty values
    # Runs on O(1)
    def __init__(self, size=40):
        self.table = []
        for i in range(size):
            self.table.append([])

    # Create hash key
    # Runs on O(1)
    def create_hash_key(self, key):
        return int(key) % len(self.table)

    # Insert each package into hash table
    # Runs on O(n).
    def insert(self, key, value):
        key_hash = self.create_hash_key(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = key_value
                    return True
            self.table[key_hash].append(key_value)
            return True

    # Lookup value in table by key
    # Runs on O(n)
    def lookup(self, key):
        index = self.create_hash_key(key)
        if self.table[index] is None:
            return None
        else:
            for kvp in self.table[index]:
                if kvp[0] == key:
                    return kvp[1]

    # Allows an item to be accessed.
    # Runs on O(1)
    def __getitem__(self, key):
        return self.table[key]

    # Allows an item to be set.
    # Runs on O(1)
    def __setitem__(self, key, value):
        self.table[key] = value

    # Allows the table to be iterated through.
    # Runs on O(1)
    def __iter__(self):
        return iter(self.table)
