from node import Node
import trie_utils

class Spelling_bee_search:
    def __init__(self, trie: Node, center_ltr, outer_ltrs):
        self.found_words = set()
        self.pangrams = set()

        self.center_ltr = center_ltr
        self.all_ltrs = center_ltr + outer_ltrs

        self.search(trie)
    

    def search(self, cur_node: Node):
        for ltr in self.all_ltrs:
            if ltr in cur_node.children:
                self.search(cur_node.children[ltr])
        
        if '>' in cur_node.children:
            word = trie_utils.reconstruct(cur_node)
            if self.center_ltr in word:
                self.found_words.add(word)
            
            is_pangram = True
            for ltr in self.all_ltrs:
                if ltr not in word:
                    is_pangram = False
            
            if is_pangram:
                self.pangrams.add(word)


    def get_found_words(self) -> list[str]:
        return list(self.found_words)

    def get_pangrams(self) -> list[str]:
        return list(self.pangrams)