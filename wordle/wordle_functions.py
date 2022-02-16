def load_words():
    """This sets a file full of words to a string

    Returns:
        list: a list of all the 5 letter words
    """
    with open('wordle/wordleWordList.txt', 'r') as f:
        words = [word[:5] for word in f]
    return words

def take_input(list_of_words):
    try:
        guess = input("Enter your 5 word guess: ")
        if guess not in list_of_words or len(guess) != 5:
            print("Error, guess has to be a valid 5 letter word")
            raise Exception()
    except:
        return take_input(list_of_words)
    return guess.lower()

def check_word(guess, actual):
    for i in range(5):
        print(i)

if __name__ == "__main__":
    wordList = load_words()
    #print(wordList[:10])
    #print(len(wordList))
    
    #guess = take_input(wordList)
    #print(guess)
    
    check_word("hello", "arose")