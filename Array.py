# Implements a 1-D Array Using the ctypes Module
import ctypes

class Array:
    # Creates the Array with the given size of the Array
    def __init__(self, size):
        assert size > 0, 'Array Must be greater than 0'
        self.size = size

        ArrayTypes = ctypes.py_object * size
        self.slots = ArrayTypes()

        self.clear(None)

    # Returns the size of the Array
    def __len__(self):
        return self.size

    # Returns the item in the given index
    def __getitem__(self, index):
        assert index >= 0 and index < len(self.slots), "Index out of range"
        return self.slots[index]

    # Sets a value to the index
    def __setitem__(self, index, value):
        assert index >= 0 and index < len(self.slots), "Index out of range"
        self.slots[index] = value

    # Sets the Value to the Array
    def clear(self, value):
        for i in range(self.size):
            self.slots[i] = value

    # Inserts value in the Index and Shifts Other Values
    def insert(self, ndx, value):
        n = len(self) - 1
        # Iterates over the Array
        for i in range(n, ndx, -1):
            # if the index value is None
            # Breaks Iteration, No need to shift
            if self[ndx] == None:
                break
            # If the value before this position is None,
            # Continue, No need to shift a None Value
            if self[i-1] == None:
                continue 
            # Shiift Value to the preceding value
            else:
                self[i] = self[i-1]
        # Inserts Value to the Free Index
        self[ndx] = value

    # Removes an index and close gap
    def pop(self, ndx):
        # Index Must be in Array
        assert ndx < len(self), "Index not in Array"
        n = len(self) - 1
        # If this is the Last Index,
        # Removes value with no shift
        if ndx == n:
            self[ndx] = None
        # Iterates the Array
        for i in range(ndx + 1, n+1):
            # if the index value is None
            # Breaks Iteration, No need to shift
            if self[ndx] == None:
                break
            # Do not Shift a None Value
            elif self[i] == None:
                continue 
            # Shifts the Value in after
            else:
                self[i-1] = self[i]
                self[i] = None
    
    # Returns Iteratable list
    def __iter__(self):
        return Arrayiterator(self.slots)



class Arrayiterator:


    # Creates the iteratable List
    def __init__(self, thelist):
        self.list = thelist
        self.idx = 0

    # Returns Iteratable Array
    def __iter__(self):
        return self.list

    # Returns next occuring Value
    def __next__(self):
        if self.idx  < len(self.list):
           let = self.list[self.idx ]
           self.idx  += 1
           return let
        else:
            raise StopIteration

