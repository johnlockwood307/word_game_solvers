class Node:
    def __init__(self, letter):
        self.letter = letter
        self.parent = None
        self.children = dict()
    
    def __str__(self):
        return self.str_helper(0)

    def str_helper(self, indent):
        return '.'*indent + self.letter + "\n" + \
            ''.join([child_node.str_helper(indent+1) for child_node in self.children.values()])