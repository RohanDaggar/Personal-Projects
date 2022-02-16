#This is a wordle clone, but made in python
from random import randint
from wordle_functions import load_words, take_input, check_word

class Cguess:
    def __init__(self, name, gy, actualWord):
        """initial creation of the class

        Args:
            name (str): the 5 letter guess
            gy (list): a list of green yellow : [0,g,r,0,r] that shows how close the guess is to the word
        """
        self.name = name
        self.ga = check_word(name, actualWord)
    

def run():
    Totalwordlist = load_words()
    winning_word = Totalwordlist[randint(0,len(Totalwordlist))]
    print(winning_word)
    guess = take_input(Totalwordlist)

if __name__ == "__main__":
    run()