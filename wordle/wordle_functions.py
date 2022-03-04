
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
            #print(f'{guess=}')
            #print(guess not in list_of_words)
            #print(f'{len(guess) = }')
            print("Guess has to be a valid 5 letter word")
            raise Exception("Error, guess has to be a valid 5 letter word")
    except:
        return take_input(list_of_words)
    return guess.lower()


def check_word(guess, actual):
    """Takes a guess word, and the actual word, and returns a string which gives information about how close the guess is to the actual word

    Args:
        guess (string): the guess word
        actual (string): the actual word of the day

    Returns:
        list: 
    """
    gy = [0,0,0,0,0]
    
    #checked_letters = []
    #greened_letters= []
    #actual_letters = {letter for letter in actual} #list of all letters in the actual word, non repeating
    #newdict = {letter:actual.count(letter) for letter in actual_letters}  #this is a count of all the letters in the guess
    
    for i in range(5):
        if guess[i] == actual[i]:
            gy[i] = 'g'
        elif guess[i] in actual:
            gy[i] = 'y'
        
    return gy

class guessWord:
    """A class which represents a guess,
    takes in (wordlist, actualWord)
    """
    def __init__(self, wordlist, actualWord):
        namei = take_input(wordlist)
        self.name = namei
        self.gy = check_word(self.name, actualWord)
    def __repr__(self):
        return self.name



def run():
    wordList = load_words()
    #print(wordList[:10])
    #print(len(wordList))
    actualWord = 'arise'
    guess = guessWord(wordList, actualWord)
    print(guess.gy)
    print(guess)
    #print("12345"[-4:])
    #print(check_word("aallo", "goose"))

if __name__ == "__main__":
    run()