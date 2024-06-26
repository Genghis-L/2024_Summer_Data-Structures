class Vector:
    """Represent a vector in a multidimensional space."""
    
    def __init__(self, d):
        """Create d-dimensional vector of zeros."""
        self.__coords = [0] * d
    
    def __len__(self):
        """Return the dimension of the vector."""
        return len(self.__coords)
    
    def __getitem__(self, j):
        """Return jth coordinate of vector."""
        return self.__coords[j]
    
    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self.__coords[j] = val
    
    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):  # relies on __len__ method
            raise ValueError("dimensions must agree")
        result = Vector(len(self))  # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    
    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self.__coords == other.coords
    
    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other  # rely on existing __eq__ definition
    
    def __str__(self):
        """Produce string representation of vector."""
        return '<' + str(self.__coords)[1:-1] + '>'  # adapt list representation

# Example usage:
v = Vector(3)
print(v)  # Output: <0, 0, 0>
v[0] = 1
v[1] = 2
v[2] = 3
print(v)  # Output: <1, 2, 3>
