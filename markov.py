import sys
import random

def make_chains(filename):
    """Takes input text as string; returns dictionary of markov chains."""

    corpus = open(filename)

    word_list = corpus.read().split()

    n = 0
    keys_list = []
    for word in word_list:
        bigram = tuple(word_list[n:(n+2)])
        keys_list.append(bigram)
        n = n + 1

    keys_list.pop()

    dictionary = {}
    i = 0
    for key in keys_list[:-1]:
        if dictionary.get(key) == None:
            dictionary[key] = [keys_list[i+1][1]]
        else:
            dictionary[key].append(keys_list[i+1][1])
        i += 1

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



#    return "Here's some random text."


print make_text(make_chains("green-eggs.txt"))

# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

# input_text = "Some text"

# # Get a Markov chain
# chain_dict = make_chains(input_text)

# # Produce random text
# random_text = make_text(chain_dict)

# # print random_text
