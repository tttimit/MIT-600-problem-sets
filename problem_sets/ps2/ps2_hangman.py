# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"
WORDLIST_TEST = "words_test.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    #print("Loading word list from file...")
    # inFile: file
    #inFile = open(WORDLIST_FILENAME, 'r')
    inFile = open(WORDLIST_TEST, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = str.split(line)
    #print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

def generate_letters():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    result = []
    for i in range(26):
        result.append(letters[i])
    return result

def show_available_letters(available_letters):
    result = ''
    for i in available_letters:
        result += i
    return result

def generate_uncomplete_word(length):
    result = ''
    for i in range(length):
        result += '_'
    return result

def collect_ans(word, un_word, guess):
    result = ''
    for i in range(len(word)):
        if guess == word[i] and un_word[i] == '_':
            result += word[i]
        else:
            result += un_word[i]
    return result
        

#print(generate_letters())
    
# your code begins here!
def hangman():
    print("Welcome to the game, Hangman!")
    word = choose_word(wordlist)
    un_word = generate_uncomplete_word(len(word))
    remaining_guesses = len(word) + 2
    print("I am thinking of a word that is " + str(len(word)) + " letters long.")
    available_letters = generate_letters()
    while remaining_guesses > 0:
        print("You have " + str(remaining_guesses) + " guesses left.")
        print("Available letters: " + show_available_letters(available_letters))
        guess = input("Please guess a letter: ")
        remaining_guesses -= 1
        available_letters.remove(guess)
        if guess in word:
            un_word = collect_ans(word, un_word, guess)
            print("Good guess: " + un_word)
        else:
            print("Oops! That letter is not in my word: " + un_word)
        print("----------")
        if un_word == word:
            print("Congratulations, you won!")
            break      
    else:
        print("Sorry, you lose! That word is " + word + '.')

hangman()
        
        
