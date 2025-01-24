class Word_path:
    # declares path, a list of row,col tuples
    def __init__(self, ltr, r, c):
        self.word = ltr
        self.path = list()
        self.add_to_path(r, c)
    
    def add_to_path(self, r, c):
        self.path.append((r,c))

    # prints word followed by comma-separated coordinates in path
    # e.g. "hello: (1, 1), (1, 0), (2, 1), (2, 2), (1, 3)"
    def __str__(self):
        result = self.word + ": "
        for coord in self.path:
            result += str(coord) + ", "
        
        return result[:-2]
