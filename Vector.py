class Vector(object):
    def __init__(self, dim, value):
        assert 0 <= value <= (1 << dim)
        self.dimension = dim
        self.value = value
        self.coveringVectors = []

    def __le__(self, other):
        assert self.dimension == other.dimension
        return self.Value & other.value == self.value

    def __lt__(self, other):
        assert self.dimension == other.dimension
        return self.value < other.value

    def __ge__(self, other):
        assert self.dimension == other.dimension
        return self.Value & other.value == other.value

    def __genCoveringVectors(self):
        for vec in range(0, 1 << self.dimension):
            if vec & self.value == self.value:
                self.coveringVectors.append( Vector(self.dimension, vec) )
    
    def __hash__(self):
        return hash((self.dimension, self.value))
    
    def __eq__(self, other):
        return self.dimension == other.dimension and self.value == other.value



    def __str__(self):
        return str(self.value)

    def getCoveringVectors(self):
        self.__genCoveringVectors()
        return self.coveringVectors


