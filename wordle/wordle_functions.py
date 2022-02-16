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
    gy = [0,0,0,0,0]
    checked_letters = []
    greened_letters= []
    
    actual_letters = {letter for letter in actual} #list of all letters in the actual word, non repeating
    newdict = {letter:actual.count(letter) for letter in actual_letters}  #this is a count of all the letters in the guess
    
    
    for i in range(5):
        if guess[i] == actual[i]:
            gy[i] = 'g' 
            greened_letters.append(guess[i])
    
    for i in range(5):
        if gy[i] == 'g':
            continue
        if guess[i] in actual:
            gy[i] = 'y'
    
    
    
    return gy


if __name__ == "__main__":
    wordList = load_words()
    #print(wordList[:10])
    #print(len(wordList))
    
    #guess = take_input(wordList)
    #print(guess)
    print("12345"[-4:])
    print(check_word("aallo", "goose"))