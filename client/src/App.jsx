import { useEffect, useState } from 'react'
import './App.css'
import { buildTrie } from './trie'
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
            <div>
                {panes.map(pane => (
                    <button
                        key={pane}
                        onClick={() => setCurPane(pane)}
                        style={{
                            backgroundColor: 'lightgray',
                            color: 'black',
                            border: (curPane == pane ? '4px solid green' : 'none')
                        }}
                    >
                        {pane}
                    </button>
                ))}
            </div>

            {/* Panes for each solver. Conditionally displayed only when that pane is active. */}
            <div style={{ display: (curPane === 'Anagrams') ? 'block' : 'none'}}>
                <AnagramsPane />
            </div>
            <div style={{ display: (curPane === 'Word Hunt') ? 'block' : 'none'}}>
                <WordHuntPane />
            </div>
        </div>
    )
}

export default App
