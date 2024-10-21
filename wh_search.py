from node import Node
import trie_utils

class Word_hunt_search:
    def __init__(self, trie: Node, letter_grid: list[list[str]]):
        self.found_words = set()
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
                    self.search(trie.children[start_ltr], r, c, covered_matrix)


    # returns a copy of the covered_matrix with the given row/col coordinate set to True
    def get_updated_covered_matrix(self, covered_matrix: list[list[bool]], 
                                   r: int, c: int) -> list[list[bool]]:
        result = covered_matrix.copy()
        result[r][c] = True
        return result

    # returns true if row,col coordinate is within the grid, or false otherwise
    def is_in_range(self, row, col):
        return 0 <= row < self.num_rows and 0 <= col < self.num_cols

    # recursively searches surrounding cells 
    def search(self, cur_node, cur_row, cur_col, covered_matrix):
        for row in range(cur_row - 1, cur_row + 2):
            for col in range(cur_col - 1, cur_col + 2):
                # don't search same cell
                # don't search if out of range
                # don't search if already covered (visited)
                if (row != cur_row or col != cur_col)\
                      and (self.is_in_range(row, col))\
                        and not covered_matrix[row][col]:
                    # continue search if it can form valid word in trie
                    ltr = self.letter_grid[row][col]
                    if ltr in cur_node.children:
                        updated_matrix = self.get_updated_covered_matrix(covered_matrix, row, col)
                        self.search(cur_node.children[ltr], row, col, updated_matrix)
                    
                    # add to found words
                    if '>' in cur_node.children:
                        self.found_words.add(trie_utils.reconstruct(cur_node))


    def get_found_words(self) -> list[str]:
        return list(self.found_words)