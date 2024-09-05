class Solution:
    def validStrings(self, n: int) -> List[str]:
        def generate(digits, i):
            if i == 0:
                res.append(''.join(digits))
                return
            
            if not digits or digits[-1] != '0':
                addDigit(digits, '0', i)
            addDigit(digits, '1', i)

        def addDigit(digits, addDigit, i):
            digits.append(addDigit)
            generate(digits, i-1)
            digits.pop()
            
        res = []
        generate([], n)
        return res
            
