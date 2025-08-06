import { buildTrie } from "./trie.js";
// buildTrie = require("./trie.js");

import { JSDOM } from 'jsdom';
// const { JSDOM } = require('jsdom');
const dom = await JSDOM.fromFile("index.html");
const document = dom.window.document;

const enterLettersTxt = document.getElementById('enterLetters');
const validityLbl = document.getElementById('validityLbl');
const anagramsOutput = document.getElementById('anagramsOutput');
let letters = "";


/**
 * Checks the validity of the inputted letters.
 * @returns whether the input letters are alphabetic and there are 6 or 7 of them.
 */
function lettersValid() {
    let letters = enterLettersTxt.value.toLowerCase();
    let regex = /^[a-z]+$/;
    let len = letters.length;
    return regex.test(letters) && (len == 6 || len == 7);
}

/**
 * Finds valid anagrams words given inputted letters. 
 * Outputs them in order of non-increasing length.
 */
function findWords() {
    if(lettersValid()) {
        validityLbl.innerHTML = "Valid.";
        anagramsOutput.innerHTML = "Words will appear here<br>and here<br>and here";
    } else {
        validityLbl.innerHTML = "Enter 6 or 7 valid letters";
    }
}


enterLettersTxt.addEventListener('input', findWords);
findWords();
let trie = buildTrie();

// setTimeout(function() {
//     anagramsOutput.innerHTML = "time up";
// }, 5000);