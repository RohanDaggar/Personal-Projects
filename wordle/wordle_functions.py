def load_words():
    with open('wordle/wordleWordList.txt', 'r') as f:
        words = [word[:-1] for word in f]
    return words



wordList = load_words()
print(wordList[:10])
print(len(wordList))