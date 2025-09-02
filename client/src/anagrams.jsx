import { useState, useEffect } from "react";
import { reconstructWord } from "./trie";

/**
 * Checks the validity of the inputted letters.
 * @returns whether the input letters are alphabetic and there are at least 6 of them.
 */
function lettersValid(letters) {
    let regex = /^[a-z]+$/;
    return regex.test(letters) && letters.length >= 6;
}

/**
 * Searches for valid anagrams words using the given letters.
 * @returns array of found words sorted by length and alphabetically.
 */
function anagramsSearch(letters, trie) {
    let wordSet = new Set()

    searchHelper(trie, letters, wordSet)
    // convert set to list, sort by decreasing length and then by alphabetical order
    return [...wordSet].sort((a, b) => b.length - a.length || a.localeCompare(b))
}

/**
 * Recursively searches for words by adding a letter, using trie to search only possible word paths.
 */
function searchHelper(curNode, remainingLetters, wordsSoFar) {
    // create a new search branch for each letter (if each path exists in the trie)
    for (const ltr of remainingLetters) {
        if (curNode.children.has(ltr)) {
            searchHelper(curNode.children.get(ltr), strSubtract(remainingLetters, ltr), wordsSoFar)
        }
    }

    // '>' character indicates this is the end of a valid word
    if (curNode.children.has('>')) {
        const word = reconstructWord(curNode)
        if (word.length >= 3) {
            wordsSoFar.add(word)
        }
    }
}

/**
 * @returns a copy of the given string with the given letter removed
 */
function strSubtract(string, ltr) {
    const ltrIndex = string.indexOf(ltr)
    if (ltrIndex >= 0) {
        return string.slice(0, ltrIndex) + string.slice(ltrIndex + 1)
    } else {
        console.log(`String ${string} does not contain letter ${ltr}`)
    }
}


export default function AnagramsPane({ trie }) {
    const [letters, setLetters] = useState('')
    const [foundWords, setFoundWords] = useState([])

    // runs on start and when letters changes
    useEffect(() => {
        if (lettersValid(letters)) {
            // do anagrams search
            setFoundWords(anagramsSearch(letters, trie))
        } else {
            setFoundWords([])
        }
    }, [letters])

    const updateResults = (e) => {
        setLetters(e.target.value)
    }

    const searchSuccessful = foundWords.length > 0
    const displayText = searchSuccessful ? foundWords.join('\n') : 'Your words will appear here'
    
    return <div>
        <h1>Anagrams</h1>
        <label>Input 6 or more alphabetic letters:</label>
        <input
            type='text'
            value={letters}
            placeholder='Your letters here'
            size='10'
            onChange={updateResults}>
        </input>
        <textarea
            value={displayText}
            rows='20'
            cols='50'
            readOnly
            style={{ color: searchSuccessful ? 'white' : 'grey' }}>
        </textarea>
    </div>
}