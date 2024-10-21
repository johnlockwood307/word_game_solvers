import sys
from node import Node
import trie_utils
import dictionary_manager
from wh_search import Word_hunt_search


eng_dict = dictionary_manager.get_eng_dict()

# filtered_words is a set of unique English words at least 3 letters long
filtered_words = set()

for word in eng_dict:
    word = word.lower()
    if len(word) >= 3:
        if word not in filtered_words:
            filtered_words.add(word)

# construct trie from filtered_words
# each word begins with '<' and ends with '>'
print("Constructing trie...")
trie = trie_utils.build_trie(filtered_words)


letter_grid = [['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l'], ['m', 'n', 'o', 'p']]

args = sys.argv

# Read letters from command line
if len(sys.argv) == 1:
    letters = input("Enter arguments: ").split()
    args = [__file__] + letters
    # print(args)

if len(args) == 2:
    letters = args.lower()
    if len(letters) not in (16, 25):
        print("Supply 16 or 25 letters. Usage:\n\tpy anagrams.py letters")
        exit(0)
    
    print(f"Reading {len(letters)} letters")
elif len(args) == 5:
    r1 = args[1].lower()
    r2 = args[2].lower()
    r3 = args[3].lower()
    r4 = args[4].lower()
    letter_grid = [[ltr for ltr in row] for row in [r1, r2, r3, r4]]

    for row in letter_grid:
        if len(row) != 4:
            print("Supply four rows of 4 letters each. Usage:\n\tpy word_hunt.py r1 r2 r3 r4")
            exit(0)
    
    print("Reading four sides of four letters")
elif len(args) == 6:
    r1 = args[1].lower()
    r2 = args[2].lower()
    r3 = args[3].lower()
    r4 = args[4].lower()
    r5 = args[5].lower()
    letter_grid = [[ltr for ltr in row] for row in [r1, r2, r3, r4, r5]]

    for row in letter_grid:
        if len(row) != 5:
            print("Supply five rows of 5 letters each. Usage:\n\tpy word_hunt.py r1 r2 r3 r4 r5")
            exit(0)
    
    print("Reading five sides of five letters")
else:
    print("Usage:\nindicate empty cells with '.'\nIf supplying four rows, each row must be 4 \
          chars long.\nIf supplying five rows, each row must be 5 chars long.\n\tpy word_hunt.py\
          \n\tpy word_hunt.py letters\n\tpy word_hunt.py row1 row2 row3 row4 [row5]")
    exit(0)


allowed_chars = "abcdefghijklmnopqrstuvwxyz."
has_illegal_chars = False

for row in letter_grid:
    for ltr in row:
        if ltr not in allowed_chars:
            has_illegal_chars = True
            print(f"Illegal char {ltr}")

if has_illegal_chars:
    exit(0)

print(f"Using {letter_grid}")




print("Searching for valid words...")
# search to find all valid words in the puzzle
search = Word_hunt_search(trie, letter_grid)

# sort found words by decreasing length and write to file
found_words = sorted(search.get_found_words(), key=lambda wrd: -len(wrd))
print(f"Found {len(found_words)} words")

with open("found_words.txt", "w") as words_file:
    for word in found_words:
        words_file.write(word + "\n")