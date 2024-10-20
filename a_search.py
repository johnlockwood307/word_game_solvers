from node import Node
import trie_utils

class Anagrams_search:
    def __init__(self, trie: Node, letters: list[str]):
        self.found_words = set()

        self.search(trie, letters)

    
    # returns a copy of the supplied list with one instance of the given element removed.
    def list_subtract(self, ltr_list: list[str], to_remove: str):
        result = ltr_list.copy()
        result.remove(to_remove)
        return result
    

    def search(self, cur_node, remaining_ltrs):
        for ltr in remaining_ltrs:
            if ltr in cur_node.children:
                self.search(cur_node.children[ltr], self.list_subtract(remaining_ltrs, ltr))
        
        if '>' in cur_node.children:
            self.found_words.add(trie_utils.reconstruct(cur_node))
    
    def get_found_words(self) -> list[str]:
        return list(self.found_words)