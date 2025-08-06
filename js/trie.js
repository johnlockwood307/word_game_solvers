// let trie;
import fs from 'fs';
import readline from 'readline';


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
        this.children = {};
    }

    getLetter() {
        return this.letter;
    }
}

/**
 * Constructs and returns trie made from dictionary words.
 */
export async function buildTrie() {
    let trie = new TrieNode('<');

    const fileStream = fs.createReadStream('./collins_scrabble_words.txt');
    const rl = readline.createInterface({input: fileStream});

    for await (const upperWord of rl) {
        let lowerWord = upperWord.toLowerCase() + '>';
        let curNode = trie;
        for (let ltr of lowerWord) {
            if(!(ltr in curNode.children)) {
                curNode.children[ltr] = new TrieNode(ltr);
                curNode.children[ltr].parent = curNode;
            }

            curNode = curNode.children[ltr];
        }
    }

    return trie;
}
