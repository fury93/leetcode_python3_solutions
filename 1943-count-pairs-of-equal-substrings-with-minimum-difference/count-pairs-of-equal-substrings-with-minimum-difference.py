class Solution:
    def countQuadruples(self, firstString: str, secondString: str) -> int:
        
        # 1. Find the first occurrence of each character in firstString.
        first = {}
        for j, char in enumerate(firstString):
            first.setdefault(char, j)
            
        # 2. Find the last occurrence of each character in secondString.
        last = {}            
        for a, char in enumerate(secondString):
            last[char] = a
        
        # 3. Find the value of (j - a) for characters that appear in both strings.
        diff_ja = defaultdict(list)
        overlap = set(firstString) & set(secondString)
        for char in overlap:
            diff_ja[first[char] - last[char]].append(char)
        
        # 4. Return the number of characters that share the minimum (j - a) value.
        mini = min(diff_ja.keys() or [0])
        return len(diff_ja[mini])