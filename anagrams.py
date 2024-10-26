import sys
import trie_utils
import dictionary_manager
from a_search import Anagrams_search


eng_dict = dictionary_manager.get_eng_dict()


letters = "abcdef"

# Read letters from command line arguments
if len(sys.argv) == 1:
    print("Using default letters")
elif len(sys.argv) == 2:
    letters = sys.argv[1]
    if len(letters) not in (6, 7):
        print("Supply 6 or 7 letters. Usage:\n\tpy anagrams.py letters")
        exit(0)
    
    print(f"Reading {len(letters)} letters")
else:
    print("Usage:\n\tpy anagrams.py\n\tpy anagrams.py letters")
    exit(0)


allowed_chars = "abcdefghijklmnopqrstuvwxyz"
has_illegal_chars = False
letters = letters.lower()
for ltr in letters:
    if ltr not in allowed_chars:
        has_illegal_chars = True
        print(f"Illegal char {ltr}")

if has_illegal_chars:
    exit(0)

print(f"Using {letters}")



# filtered_words is a set of unique English words 3 to 6/7 letters long
filtered_words = set()

for word in eng_dict:
    word = word.lower()
    if len(word) >= 3 and len(word) <= len(letters):
        if word not in filtered_words:
            filtered_words.add(word)



# construct trie from filtered_words
# each word begins with '<' and ends with '>'
print("Constructing trie...")
trie = trie_utils.build_trie(filtered_words)

print("Searching for valid words...")
# search to find all valid words in the puzzle
search = Anagrams_search(trie, [ltr for ltr in letters])

# sort found words by decreasing length and write to file
found_words = sorted(search.get_found_words(), key=lambda wrd: -len(wrd))
print(f"Found {len(found_words)} words")

with open("found_words.txt", "w") as words_file:
    for word in found_words:
        words_file.write(word + "\n")