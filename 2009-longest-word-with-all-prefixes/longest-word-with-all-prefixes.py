class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        longest_valid_word = ""

        # Insert all words into the trie
        for word in words:
            trie._insert(word)

        # Check each word and update the longest valid word
        for word in words:
            if trie._has_all_prefixes(word):
                if len(word) > len(longest_valid_word) or (
                    len(word) == len(longest_valid_word)
                    and word < longest_valid_word
                ):
                    longest_valid_word = word

        return longest_valid_word


class Trie:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.is_end_of_word = False

    def __init__(self):
        self.root = self.TrieNode()

    # Insert a word into the trie
    def _insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = self.TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    # Check if all prefixes of the word exist in the trie
    def _has_all_prefixes(self, word):
        node = self.root
        for char in word:
            if (
                char not in node.children
                or not node.children[char].is_end_of_word
            ):
                return False
            node = node.children[char]
        return True