from node import Node
from word_path import Word_path
import trie_utils
from copy import deepcopy

class Word_hunt_search:
    def __init__(self, trie: Node, letter_grid: list[list[str]]):
        # set of found words
        self.found_words = set()
        # set of Word_path objects, containing the word and a list of
        # row,col coordinates making up the word's path through the grid
        self.found_word_paths = set()
        self.letter_grid = letter_grid

        self.num_rows = len(self.letter_grid)
        self.num_cols = len(self.letter_grid[0])
        
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                start_ltr = self.letter_grid[r][c]
                
                covered_matrix = [[False for j in range(self.num_cols)] for i in range(self.num_rows)]
                covered_matrix[r][c] = True

                # initiate search starting at this cell if it is a valid letter (not .)
                if self.letter_grid[r][c] in trie.children:
                    word_path = Word_path(start_ltr, r, c)
                    self.search(trie.children[start_ltr], r, c, covered_matrix, word_path)


    # returns a copy of the covered_matrix with the given row/col coordinate set to True
    def get_updated_covered_matrix(self, covered_matrix: list[list[bool]], 
                                   r: int, c: int) -> list[list[bool]]:
        result = deepcopy(covered_matrix)
        result[r][c] = True
        return result

    # returns true if row,col coordinate is within the grid, or false otherwise
    def is_in_range(self, row, col):
        return 0 <= row < self.num_rows and 0 <= col < self.num_cols

    # recursively searches surrounding cells 
    def search(self, cur_node, cur_row, cur_col, covered_matrix, word_path):
        for row in range(cur_row - 1, cur_row + 2):
            for col in range(cur_col - 1, cur_col + 2):
                # don't search if out of range
                # don't search if already covered (visited)
                if (self.is_in_range(row, col))\
                      and not covered_matrix[row][col]:

                    # continue search if it can form valid word in trie
                    ltr = self.letter_grid[row][col]
                    if ltr in cur_node.children:
                        new_word_path = deepcopy(word_path)
                        new_word_path.word += ltr
                        new_word_path.add_to_path(row, col)

                        self.search(cur_node.children[ltr], row, col, \
                                    self.get_updated_covered_matrix(covered_matrix, row, col), \
                                        new_word_path)

        # add to found words if not already there
        if '>' in cur_node.children:
            if word_path.word not in self.found_words:
                self.found_words.add(word_path.word)
                self.found_word_paths.add(word_path)


    def get_found_words(self) -> list[str]:
        return list(self.found_words)
    
    def get_found_word_paths(self) -> list[Word_path]:
        return list(self.found_word_paths)


    def print_matrix(self, covered_matrix):
        result_str = ""

        for row in covered_matrix:
            for bool in row:
                if bool:
                    result_str += '1'
                else:
                    result_str += '0'
            result_str += '\n'
        
        print(result_str)