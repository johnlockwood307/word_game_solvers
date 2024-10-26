import sys
import trie_utils
import dictionary_manager
from sb_search import Spelling_bee_search


eng_dict = dictionary_manager.get_eng_dict()

# filtered_words is a set of unique English words at least 3 letters long
filtered_words = set()

for word in eng_dict:
    word = word.lower()
    if len(word) >= 4:
        if word not in filtered_words:
            filtered_words.add(word)

# construct trie from filtered_words
# each word begins with '<' and ends with '>'
print("Constructing trie...")
trie = trie_utils.build_trie(filtered_words)


letters = "Abcdefg"

args = sys.argv

# Read letters from command line
if len(sys.argv) == 1:
    letters = input("Enter arguments: ").split()
    args = [__file__] + letters

if len(args) == 2:
    letters = args[1]
    if len(letters) != 7:
        print("Supply 7 letters. Usage:\n\tpy spelling_bee.py Letters")
        exit(0)
else:
    print("Usage: indicate center letter with capital letter, or as first letter.\
          \n\tpy spelling_bee.py Letters")
    exit(0)


allowed_chars_lc = "abcdefghijklmnopqrstuvwxyz"
allowed_chars_uc = allowed_chars_lc.upper()

center_ltr = None
outer_ltrs = None
num_uc = 0
has_illegal_chars = False
has_duplicates = False
char_set = set()

for ltr in letters:
    if ltr in char_set:
        print(f"Duplicate char {ltr}")
        has_duplicates = True
    else:
        char_set.add(ltr)

    if ltr in allowed_chars_uc:
        num_uc += 1
        center_ltr = ltr
    elif ltr not in allowed_chars_lc:
        print(f"Illegal char {ltr}")
        has_illegal_chars = True

if has_illegal_chars or has_duplicates:
    exit(0)

if num_uc == 0:
    print(f"No capital letters given.\nUsing {letters[0]} as center letter and {letters[1:]} as outer letters.")
    center_ltr = letters[0]
    outer_ltrs = letters[1:]
elif num_uc == 1:
    outer_ltrs = letters.replace(center_ltr, "")
    print(f"Using {center_ltr} as center letter and\
          {outer_ltrs} as outer letters.")
elif num_uc > 1:
    print(f"Multiple capital letters given.\nUsing {letters[0]} as center letter and {letters[1:]} as outer letters.")
    center_ltr = letters[0]
    outer_ltrs = letters[1:]


center_ltr = center_ltr.lower()
outer_ltrs = outer_ltrs.lower()



print("Searching for valid words...")
# search to find all valid words in the puzzle
search = Spelling_bee_search(trie, center_ltr, outer_ltrs)


# sort found words by decreasing length and write to file
found_words = sorted(search.get_found_words(), key=lambda wrd: -len(wrd))
print(f"Found {len(found_words)} words")

with open("found_words.txt", "w") as words_file:
    for word in found_words:
        words_file.write(word + "\n")


pangrams = sorted(search.get_pangrams(), key=lambda wrd: -len(wrd))
print(f"Found {len(pangrams)} pangrams")

with open("pangrams.txt", "w") as pangrams_file:
    for word in pangrams:
        pangrams_file.write(word + "\n")
