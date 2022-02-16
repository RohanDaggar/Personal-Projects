from wordle_functions import load_words

def test_load_words():
    wordList = load_words()
    assert type(wordList) == list
    for word in wordList:
        print(word)
        assert type(word) == str
        assert len(word) == 5