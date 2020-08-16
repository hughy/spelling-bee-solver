#!/usr/bin/env python
"""
Uses breadth-first search to find all valid words in a set of seven letters.

The definition of a "valid" word follows from the rules of the New York Times
Spelling Bee Game:

1. The word contains the "center" letter (designated here as the first letter in the
input list)
2. The word is at least four letters in length
3. The word is in the dictionary (the dictionary here is defined by the list of words
in dictionary.txt)
4. A word may use a letter more than once

Since a valid word may be arbitrarily long it is necessary to search for prefixes in
the dictionary in order to terminate the search.
"""
import argparse
import string
from collections import deque
from typing import List

from spelling_bee_solver import trie


def solve(letters: List[str], dictionary: trie.Node) -> List[str]:
    """Finds all words that can be made using the given letters.
    """
    center_letter = letters[0]
    words = set()

    queue = deque([letter for letter in letters])
    while queue:
        candidate = queue.popleft()
        is_word, is_prefix = trie.has_word_has_prefix(dictionary, candidate)
        if is_word and center_letter in candidate:
            words.add(candidate)
        if is_prefix:
            queue.extend([candidate + letter for letter in letters])

    return list(words)


def get_dictionary() -> trie.Node:
    """Reads the dictionary text file into a trie.
    """
    dictionary = {}
    with open("dictionary.txt", "r") as f:
        for line in f:
            word = line.strip()
            if len(word) >= 4:
                trie.insert(dictionary, word)

    return dictionary


def main(letters: List[str]) -> None:
    dictionary = get_dictionary()
    words = solve(letters, dictionary)

    sorted_words = sorted(words, key=lambda word: (len(word), word))
    print("\n".join(sorted_words))


def validate_letters(letters: List[str]) -> None:
    """Confirms the all input letters are unique and uppercase letters.
    """
    letter_set = set(letters)
    if len(letter_set) != 7:
        raise ValueError("All seven letters must be unique!")

    if not letter_set.issubset(set(string.ascii_uppercase)):
        raise ValueError("Only uppercase letters are allowed!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Solve the NYT Spelling Bee game")
    parser.add_argument(
        "letters",
        type=str,
        nargs=7,
        help="""
        The seven letters in the 'hive'. The first letter should be the letter
        from the center of the 'hive'.""".strip(),
    )
    args = parser.parse_args()
    validate_letters(args.letters)
    main(args.letters)
