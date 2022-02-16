def load_words():
    with open('wordle/wordleWordList.txt', 'r') as f:
        words = [word[:5] for word in f]
    return words


if __name__ == "__main__":
    wordList = load_words()
    print(wordList[:10])
    print(len(wordList))