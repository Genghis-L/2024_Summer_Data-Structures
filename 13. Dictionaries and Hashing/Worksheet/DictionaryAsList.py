# Python built-in methods are used, capacity is not considered

from DictionaryADT import DictionaryADT


class DictionaryAsDoubleList(DictionaryADT):
    """
    A DictionaryAsDoubleList (DADL) stores keys and values separately.
    It uses two Python lists of identical size:
        _keys stores all the keys
        _values store all the values
    For any KV item (k, v) in the DADL, the index of k in _keys
    corresponds to the index of v in _values.
    """

    def __init__(self):
        self._keys = []
        self._values = []

    def __len__(self):
        return len(self._keys)

    def __contains__(self, k):
        return k in self._keys

    def __iter__(self):
        self._iter = 0
        return self

    def __next__(self):
        if self._iter >= len(self):
            raise StopIteration
        else:
            k = self._keys[self._iter]
            self._iter += 1
            return k

    def __str__(self):
        s = "["
        for i in range(len(self)):
            s += "(" + str(self._keys[i]) + "," + str(self._values[i]) + ")"
        s += "]"
        return s

    """
    Inserts a new KV item in the DADL.
    """

    def put(self, k, v):
        # TODO
        pos = self._keys.find(k)
        if pos == -1:
            self._keys.append(k)
            self._values.append(v)
        else:
            self._values[pos] = v

    """
    Looks for a KV item whose key matches k in the DADL.
    Returns the value of the item if found in the DADL, None otherwise.
    """

    def get(self, k):
        # TODO
        pos = self._keys.find(k)
        if pos == -1:
            return None
        else:
            return self._values[pos]

    """
    Looks for a KV item whose key matches k and removes it from the DADL.
    Returns the value of the item if found and removed from the DADL, None otherwise.
    """

    def remove(self, k):
        # TODO
        pos = self._keys.find(k)
        if pos == -1:
            return None
        else:
            del_value = self._values[pos]
            self._keys[pos], self._values[pos] = self._keys.pop(), self._values.pop()
        return del_value

    """
    Deletes all the values in the DADL.
    """

    def clear(self):
        del self._keys[:]
        del self._values[:]
