import pytest

from spelling_bee_solver import trie


@pytest.fixture
def test_trie():
    return {"t": {"e": {"s": {"t": {trie.END_OF_WORD: {}}}}}}


def test_insert(test_trie):
    test_node = {}

    trie.insert(test_node, "test")
    assert test_node == test_trie


def test_has_word(test_trie):
    assert trie.has_word(test_trie, "test")
    assert not trie.has_word(test_trie, "tests")


def test_has_prefix(test_trie):
    assert trie.has_prefix(test_trie, "t")
    assert trie.has_prefix(test_trie, "test")
    assert not trie.has_prefix(test_trie, "ta")
