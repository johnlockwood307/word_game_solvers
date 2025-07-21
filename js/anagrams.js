const enterLettersTxt = document.getElementById('enterLetters')
const validityLbl = document.getElementById('validityLbl')
const anagramsOutput = document.getElementById('anagramsOutput')
let letters = ""

enterLettersTxt.addEventListener('input', findWords)

findWords()


/**
 * Checks the validity of the inputted letters.
 * @returns whether the input letters are alphabetic and there are 6 or 7 of them.
 */
function lettersValid() {
    letters = enterLettersTxt.value.toLowerCase()
    regex = /^[a-z]+$/
    len = letters.length
    return regex.test(letters) && (len == 6 || len == 7)
}

/**
 * Finds valid anagrams words given inputted letters. 
 * Outputs them in order of non-increasing length.
 */
function findWords() {
    if(lettersValid()) {
        validityLbl.innerHTML = "Valid."
        anagramsOutput.innerHTML = "Words will appear here<br>and here<br>and here"
    } else {
        validityLbl.innerHTML = "Enter 6 or 7 valid letters"
    }
}