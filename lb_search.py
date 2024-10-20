from node import Node
import trie_utils

class Letter_boxed_search:    
    def __init__(self, trie: Node, s1: str, s2: str, s3: str, s4: str):
        self.found_words = []
        self.sides = [s1, s2, s3, s4]

        for side in self.sides:
            for start_ltr in side:
                self.search(side, trie.children[start_ltr])

    # returns the three sides the one supplied as an argument
    def get_possible_next_sides(self, side: str):
        sides = self.sides.copy()
        if side in sides:
            sides.remove(side)
            return sides
        else:
            raise RuntimeError("invalid side supplied to get_possible_next_ltrs")

    # searches for valid words and adds them to found_words
    def search(self, cur_side: str, cur_node: Node):
        # recursively search valid paths from here
        for side in self.get_possible_next_sides(cur_side):
            for ltr in side:
                if ltr in cur_node.children:
                    self.search(side, cur_node.children[ltr])
        
        if '>' in cur_node.children:
            self.found_words.append(trie_utils.reconstruct(cur_node))
    

    def get_found_words(self) -> list[str]:
        return self.found_words