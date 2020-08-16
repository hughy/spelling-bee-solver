import pytest

from spelling_bee_solver import __version__
from spelling_bee_solver import solver
from spelling_bee_solver import trie


def test_version():
    assert __version__ == "0.1.0"


def test_get_dictionary():
    dictionary = solver.get_dictionary()

    with open("dictionary.txt") as f:
        for line in f:
            word = line.strip()
            if len(word) >= 4:
                assert trie.has_word(dictionary, word)


def test_solve():
    words = ["FINE", "FELINE", "LIFE", "LINE", "LIFELINE", "NINE"]

    letters = ["E", "F", "I", "L", "N"]

    dictionary = {}
    for word in words:
        trie.insert(dictionary, word)

    solved_words = solver.solve(letters, dictionary)

    assert set(solved_words) == set(words)


def test_solve_no_duplicates():
    dictionary = {"T": {"E": {"S": {"T": {trie.END_OF_WORD: {}}}}}}

    # We should not allow duplicate letters, but `solve` should still find only unique words
    letters = ["T", "E", "S", "T"]

    solved_words = solver.solve(letters, dictionary)
    assert solved_words == ["TEST"]


def test_validate_letters_unique():
    with pytest.raises(ValueError):
        solver.validate_letters(["A", "A"])


def test_validate_letters_non_uppercase():
    with pytest.raises(ValueError):
        solver.validate_letters(["a"])

    with pytest.raises(ValueError):
        solver.validate_letters(["1"])
