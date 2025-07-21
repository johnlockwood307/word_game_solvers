from node import Node

# builds and returns the trie out of the supplied words
def build_trie(words) -> Node:
    trie = Node('<')

    for word in words:
        word += '>'
        cur_node = trie

        # add letter path to trie if it does not exist already
        for ltr in word:
            if ltr not in cur_node.children:
                cur_node.children[ltr] = Node(ltr)
                cur_node.children[ltr].parent = cur_node
            
            cur_node = cur_node.children[ltr]
    
    return trie


# reconstructs a word in the trie backwards from the last letter (before >)
def reconstruct(node: Node) -> str:
    cur_node = node
    word = ""
    while cur_node.letter != '<':
        word = cur_node.letter + word
        cur_node = cur_node.parent
    
    return word
