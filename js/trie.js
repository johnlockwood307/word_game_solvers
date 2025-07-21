let trie;

class TrieNode {
    constructor(letter) {
        this.letter = letter;
        this.parent = NaN;
        this.children = {}
    }
}

function buildTrie() {
    trie = TrieNode('<')
}