let trie;
import fs from 'fs';
import readline from 'readline';


class TrieNode {
    constructor(letter) {
        this.letter = letter;
        this.parent = NaN;
        this.children = {};
    }
}

async function buildTrie() {
    trie = TrieNode('<');

    const fileStream = fs.createReadStream('../collins_scrabble_words.txt');
    const rl = readline.createInterface({input: fileStream});

    for await (const upperWord of rl) {
        lowerWord = upperWord.toLowerCase() + '>';
        let curNode = trie;
        for (let ltr of lowerWord) {
            if(!(ltr in curNode.children)) {
                curNode.children[ltr] = TrieNode(ltr);
                curNode.children[ltr].parent = curNode;
            }

            curNode = curNode.children[ltr];
        }
    }
}
