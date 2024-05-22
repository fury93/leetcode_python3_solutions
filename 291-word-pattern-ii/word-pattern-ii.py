class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        symbols = [""] * 26
        word_set = set()

        def is_match(s_index: int, p_index: int):
            # Base case: reached end of pattern
            if p_index == len(pattern):
                return s_index == len(s)  # True if and only if also reached end of s

            # Get current pattern character
            symbol = pattern[p_index]

            # This symbol already has an associated word
            if symbols[ord(symbol) - ord("a")]:
                word = symbols[ord(symbol) - ord("a")]
                # Check if it matches s[s_index...s_index + len(word)]
                if s[s_index : s_index + len(word)] != word:
                    return False
                # If it matches continue to match the rest
                return is_match(s_index + len(word), p_index + 1)

            # Count the number of spots the remaining symbols in the pattern take
            filled_spots = 0
            for i in range(p_index + 1, len(pattern)):
                if symbols[ord(pattern[i]) - ord("a")]:
                    filled_spots += len(symbols[ord(pattern[i]) - ord("a")])
                else:
                    filled_spots += 1

            # This symbol does not have an associated word
            for k in range(s_index + 1, len(s) - filled_spots + 1):
                new_word = s[s_index:k]
                if new_word in word_set:
                    continue
                # Create or update it
                symbols[ord(symbol) - ord("a")] = new_word
                word_set.add(new_word)
                # Continue to match the rest
                if is_match(k, p_index + 1):
                    return True
                # Backtracking
                symbols[ord(symbol) - ord("a")] = ""
                word_set.remove(new_word)
            # No mappings were valid
            return False

        return is_match(0, 0)