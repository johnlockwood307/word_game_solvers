/**
 * Node containing a letter within the trie representing all dictionary words
 * Special nodes:
 *     < is the root node.
 *     > is a leaf node. Its direct parent is the last letter of a word.
 */
class TrieNode {
    constructor(letter) {
        this.letter = letter;
        this.parent = NaN;
        this.children = new Map();
    }
}

/**
 * Constructs and returns trie made from dictionary words.
 */
export function buildTrie(wordArr) {
    let trie = new TrieNode('<')

    for (const word of wordArr) {
        let curNode = trie
        // add special character '>' to denote end of word
        for (const letter of (word + '>')) {
            // if the trie does not contain this letter branch, create a new child node.
            if (!curNode.children.has(letter)) {
                const newChildNode = new TrieNode(letter)
                newChildNode.parent = curNode
                curNode.children.set(letter, newChildNode)
            }

            // updates curNode to the child node for the next iteration (following letter)
            curNode = curNode.children.get(letter)
        }
    }

    return trie
}

/**
 * Given the node of the last letter in a word, reconstructs and returns the word.
 */
export function reconstructWord(endNode) {
    let curNode = endNode
    let word = ''
    
    while (curNode.letter != '<') {
        word = curNode.letter + word
        curNode = curNode.parent
    }

    return word
}