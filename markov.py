import sys
import random

script,filename = sys.argv

def make_chains(filename):
    """Takes input text as string; returns dictionary of markov chains."""

    corpus = open(filename)

    word_list = corpus.read().split()
    dictionary = {}

    for i in range(len(word_list)-2):
        key = (word_list[i], word_list[i+1])
        dictionary.setdefault(key, []).append(word_list[i+2])
  
    return dictionary



def make_text(dictionary):
    """Takes dictionary of markov chains; returns random text."""

   
    starting_key = random.choice(dictionary.keys())         # choose key (tuple) to start at
    new_text_list = list(starting_key)                       # add items in that tuple to list of created text
   
    while dictionary.get(starting_key) != None:
        value_list = dictionary[starting_key]               # assign value of key (list)
        rand_index = random.randrange(0, len(value_list))   # choose random int w/in length of list
        next_word = value_list[rand_index]                  # find item at that random index
        
        new_text_list.append(next_word)                     # add next_word to list of created text

        starting_key = (starting_key[1], next_word)         # create new tuple from second word of previous tuple + item at that index
        
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
