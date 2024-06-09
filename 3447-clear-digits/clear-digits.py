class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch.isalpha():
                stack.append(ch)
            elif stack:
                stack.pop()

        return ''.join(stack)