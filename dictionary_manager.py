import english_dictionary
import english_words

options = ["english_dictionary", "english-words", "collins_scrabble_words"]

# returns a set of unique lowercase words
def get_eng_dict(dict_name="collins_scrabble_words") -> set[str]:
    # obtain raw_dict: iter[str]
    match dict_name:
        case "english_dictionary":
            raw_dict = english_dictionary.scripts.read_pickle.get_dict()
        case "english-words":
            raw_dict = english_words.get_english_words_set(['web2'], lower=True)
        case "collins_scrabble_words":
            raw_dict = list()
            with open("collins_scrabble_words.txt", "r") as scrabble_words:
                cur_line = scrabble_words.readline().strip()
                while cur_line != "":
                    raw_dict.append(cur_line)
                    cur_line = scrabble_words.readline().strip()
        case _:
            raise RuntimeError(f"dict_name {dict_name} not recognized.\nOptions: {options}")
    
    # convert raw_dict to eng_dict, a set of unique lowercase strings
    eng_dict = set()
    for word in raw_dict:
        eng_dict.add(word.lower())
    
    return eng_dict
