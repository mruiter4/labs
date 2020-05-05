"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    #with keyword automatically closes the file
    with open(file_path) as file:
        #file.read() returns the entire file as a string
        return file.read()


def make_chains(input_text):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = input_text.split()
    for i in range(len(words)-2):
        #create a key
        key = (words[i], words[i+1])

        #make chains
        #if the key already exists in chains: 
            #append the next word (words[i+2]) to the list
        #else 
            #add the key and assign value to new list
        if key in chains:
            chains[key].append(words[i+2])
        else:
            chains[key] = [words[i+2]]   

    return chains


def make_text(chains):
    """Return text from chains"""
    
    words = []

    #get a random link from the dictionary and add to words list
    #choice requires a sequence as input
    link = (choice(list(chains.keys())))
    words.extend(link)
    #get an additional word from the value list of the random key; add to list
    additional_word = choice(chains[link])
    words.append(additional_word)
    
    while True:
        link = (link[1], additional_word)
        if link in chains:
            additional_word = choice(chains[link])
            words.append(additional_word)
        else:
            break

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
