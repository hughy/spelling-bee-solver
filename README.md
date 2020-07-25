# spelling-bee
Spelling Bee is a word game from the New York Times.

https://www.nytimes.com/puzzles/spelling-bee

## Rules
Players create words from a bank of seven different letters arranged into a honey-comb shape (the "hive"). All words must use the central letter and must be at least four letters in length. Words may use any letters more than once.

## Solver
This Python package implements an automatic solver for the Spelling Bee game. Given a list of seven letters (with the "central letter" listed first) the solver identifies all valid words that a player can create according to the rules of the game.

Note thate the dictionary that the solver uses may not be the same as the dictionary that the New York Times uses. The dictionary contained in dictionary.txt is the "SOWPODS" dictionary (https://en.wikipedia.org/wiki/Collins_Scrabble_Words).

## Usage
This project uses `poetry` to manage dependencies and virtual environments.

To run unit tests run

    poetry run pytest

To run the solver program run

    poetry run python -m spelling_bee_solver.solver <A> <B> <C> <D> <E> <F> <G>

replacing `<A> <B> <C> <D> <E> <F> <G>` with the seven letters to use in the game.