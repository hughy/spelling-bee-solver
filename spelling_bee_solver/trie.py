"""
Implements a trie data structure:

https://en.wikipedia.org/wiki/Trie

I use a dict to represent each node in the trie, with keys mapped to descendant nodes.
The sequence "EOW" represents the end of a word and indicates that the path from the
root of the trie to that node spells out a valid word. For instance, insertion of the
word "CAT" into an empty dict results in the following:

    {
        "C": {
            "A": {
                "T": {
                    "EOW": {}
                }
            }
        }
    }

The design of the implementations of the functions in this module treats `_find` and
`insert` as algorithms applied to a graph data structure rather than methods of a
`Trie` type. Python's `heapq` module inspires this approach.

The trie data structure in this package only stores keys, so the generalized graph node

    class Node:

        edges: Dict[str, Any]
        value: Any

is reduced to the simple dict mapping type alias

    Node = Dict[str, "Node"]
"""
from typing import Dict
from typing import Tuple


Node = Dict[str, "Node"]


END_OF_WORD = "EOW"


def has_word(trie: Node, word: str) -> bool:
    """Determines whether the trie contains the given word.
    """
    word_node = _find(trie, word)
    return END_OF_WORD in word_node


def has_prefix(trie: Node, prefix: str) -> bool:
    """Determines whether the trie contains any word that starts with the given prefix.
    """
    prefix_node = _find(trie, prefix)
    return prefix_node != {}


def has_word_has_prefix(trie: Node, key: str) -> Tuple[bool, bool]:
    """Determines both whether the trie contains a key as a word and as a prefix.
    """
    key_node = _find(trie, key)
    trie_has_word = END_OF_WORD in key_node
    trie_has_prefix = key_node != {}
    return trie_has_word, trie_has_prefix


def _find(trie: Node, key: str) -> Node:
    """Finds the node in the trie for the given key.
    """
    if not key:
        return trie

    head, tail = key[:1], key[1:]
    if head not in trie:
        return {}

    return _find(trie[head], tail)


def insert(trie: Node, word: str) -> None:
    """Inserts the given word into the trie.
    """
    if not word:
        trie[END_OF_WORD] = {}
        return

    head, tail = word[:1], word[1:]
    if head not in trie:
        trie[head] = {}
    
    insert(trie[head], tail)
