import { useEffect, useState } from 'react'
import './App.css'
import { buildTrie } from './trie'
import ButtonPane from './topButtonPane'
import AnagramsPane from './anagrams'
import WordHuntPane from './wordHunt'


function App() {
    const panes = ['Anagrams', 'Word Hunt']
    const [curPane, setCurPane] = useState(panes[0]) // default pane
    const [trie, setTrie] = useState(null)

    // fetch dictionary words from text file and use them to build the trie
    useEffect(() => {
        fetch('/collins_scrabble_words.txt')
            .then((res) => res.text())
            .then((text) => {
                const words = text
                    .split('\n')                                // turns text into array of words
                    .map((w) => w.trim().toLowerCase())         // removes newlines, makes lower case
                    .filter(Boolean)                            // removes any falsy values
                
                setTrie(buildTrie(words))
            })
    }, [])                                      // empty dependency array ensures fetch only runs once

    return (
        <div>
            {/* Top button pane */}
            <ButtonPane panes={panes} curPane={curPane} setCurPane={setCurPane}/>

            {/* Panes for each solver. Conditionally displayed only when that pane is active. */}
            <div style={{ display: (curPane === 'Anagrams') ? 'block' : 'none'}}>
                <AnagramsPane trie={trie}/>
            </div>
            <div style={{ display: (curPane === 'Word Hunt') ? 'block' : 'none'}}>
                <WordHuntPane trie={trie}/>
            </div>
        </div>
    )
}

export default App
