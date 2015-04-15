import sys
import random

script, filename, ngram = sys.argv                          # unpack sys.argv arguments

def make_chains(filename, ngram):
    """Takes input text as string; returns dictionary of markov chains."""

    corpus = open(filename)

    word_list = corpus.read().split()                           # read in text of file as a list
    dictionary = {}                                             # initialize empty dictionary

    n = int(ngram)                                              # set n (number of items in tuples)
    for i in range(len(word_list)-n):                           # loop over list items to fill dictionary
        key = tuple(word_list[i:(i+n)])                         # make keys in dictionary tuples of n items
        dictionary.setdefault(key, []).append(word_list[i+n])   # use setdefault to create values of dictionary
    
    return dictionary



def make_text(dictionary):
    """Takes dictionary of markov chains; returns random text."""

    capital_keys_list = [key for key in dictionary.keys() if key[0][0].isupper()]   # create list of only keys that start with an uppercase letter
    starting_key = random.choice(capital_keys_list)             # choose key (tuple) to start at
    new_text_list = list(starting_key)                          # add items in that tuple to list of created text
   
    punctuation = "?.!"                                         # create punctuation string    
    next_word = " "                                             # initialize next_word

    while dictionary.get(starting_key) != None and next_word[-1] not in punctuation: # Continue until the key is not found in the dictionary and until the last word ends in punctuation
        value_list = dictionary[starting_key]               # assign value of key (list)
        rand_index = random.randrange(0, len(value_list))   # choose random int w/in length of list
        next_word = value_list[rand_index]                  # find item at that random index

        new_text_list.append(next_word)                     # add next_word to list of created text

        starting_key = tuple(list(starting_key[1:]) + [next_word])   # create new tuple from second word of previous tuple + item at that index

    new_text_string = " ".join(new_text_list)               # join list into string
    return new_text_string                                  # return new text



def main():                                                 # define main function
    input_text = filename
    chain_dict = make_chains(input_text, ngram)             # Get a Markov chain
    random_text = make_text(chain_dict)                     # Produce random text

    print random_text

if __name__ == "__main__":                                  # main() will only run if program is run directly
    main()
