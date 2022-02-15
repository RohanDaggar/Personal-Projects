from wordle_word_finder import load_words

def test_load_words():
    assert type(load_words()) == str