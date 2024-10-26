import sys
import trie_utils
import dictionary_manager
from lb_search import Letter_boxed_search


eng_dict = dictionary_manager.get_eng_dict()


s1 = "abc"
s2 = "def"
s3 = "ghi"
s4 = "jkl"

# Read letters from command line arguments
if len(sys.argv) == 1:
    print("Using default letters")
elif len(sys.argv) == 2:
    letters = sys.argv[1]
    if len(letters) != 12:
        print("Supply 12 letters. Usage:\n\tpy letter_boxed.py letters")
        exit(0)
    
    print("Reading twelve letters")
    s1 = letters[0:3]
    s2 = letters[3:6]
    s3 = letters[6:9]
    s4 = letters[9:12]
elif len(sys.argv) == 5:
    s1 = sys.argv[1]
    s2 = sys.argv[2]
    s3 = sys.argv[3]
    s4 = sys.argv[4]
    
    for side in s1, s2, s3, s4:
        if len(side) != 3:
            print("Supply four sides of 3 letters each. Usage:\n\tpy letter_boxed.py s1 s2 s3 s4")
            exit(0)
    
    print("Reading four sides of three letters")
else:
    print("Usage:\n\tpy letter_boxed.py\n\tpy letter_boxed.py letters\n\tpy letter_boxed.py side1 side2 side3 side4")
    exit(0)


allowed_chars = "abcdefghijklmnopqrstuvwxyz"
has_illegal_chars = False
s1 = s1.lower()
s2 = s2.lower()
s3 = s3.lower()
s4 = s4.lower()
for side in s1, s2, s3, s4:
    for ltr in side:
        if ltr not in allowed_chars:
            has_illegal_chars = True
            print(f"Illegal char {ltr}")

if has_illegal_chars:
    exit(0)

print(f"Using {s1} {s2} {s3} {s4}")



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

print("Searching for valid words...")
# search to find all valid words in the puzzle
search = Letter_boxed_search(trie, s1, s2, s3, s4)

# sort found words by decreasing length and write to file
found_words = sorted(search.get_found_words(), key=lambda wrd: -len(wrd))
print(f"Found {len(found_words)} words")

with open("found_words.txt", "w") as words_file:
    for word in found_words:
        words_file.write(word + "\n")