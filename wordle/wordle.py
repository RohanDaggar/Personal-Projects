#This is a wordle clone, but made in python
from random import randint
from wordle_functions import load_words, guessWord


    

def run():
    Totalwordlist = load_words()
    winning_word = Totalwordlist[randint(0,len(Totalwordlist))]
    print(winning_word)
    guess = guessWord(Totalwordlist, winning_word)

if __name__ == "__main__":
    run()