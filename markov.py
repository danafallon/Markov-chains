import sys
import random

script,filename = sys.argv

def make_chains(filename):
    """Takes input text as string; returns dictionary of markov chains."""

    corpus = open(filename)

    word_list = corpus.read().split()
    dictionary = {}

    n = 3
    for i in range(len(word_list)-n):
        key = tuple(word_list[i:(i+n)])
        dictionary.setdefault(key, []).append(word_list[i+n])
    
    return dictionary



def make_text(dictionary):
    """Takes dictionary of markov chains; returns random text."""

    capital_keys_list = [key for key in dictionary.keys() if key[0][0].isupper()]
    starting_key = random.choice(capital_keys_list)         # choose key (tuple) to start at
    new_text_list = list(starting_key)                       # add items in that tuple to list of created text
   
    punctuation = "?.!"
    next_word = " "

    while dictionary.get(starting_key) != None and next_word[-1] not in punctuation:
        value_list = dictionary[starting_key]               # assign value of key (list)
        rand_index = random.randrange(0, len(value_list))   # choose random int w/in length of list
        next_word = value_list[rand_index]                  # find item at that random index

        new_text_list.append(next_word)                     # add next_word to list of created text

        starting_key = tuple(list(starting_key[1:]) + [next_word])   # create new tuple from second word of previous tuple + item at that index

    new_text_string = " ".join(new_text_list)
    return new_text_string


# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

input_text = filename

# Get a Markov chain
chain_dict = make_chains(input_text)

# Produce random text
random_text = make_text(chain_dict)

print random_text
