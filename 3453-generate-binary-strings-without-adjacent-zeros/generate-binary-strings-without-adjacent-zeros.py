class Solution:
    def validStrings(self, n: int) -> List[str]:
        def generate(i):
            if i == n:
                res.append(''.join(map(str,digits)))
                return
            
            if digits[i-1] != 0:
                digits[i] = 0
                generate(i+1)
                #addDigit(digits, '0', i)
            digits[i] = 1
            generate(i+1)
            #addDigit(digits, '1', i)

        def addDigit(digits, addDigit, i):
            digits.append(addDigit)
            generate(digits, i-1)
            digits.pop()
            
        res, digits = [], [None] * n
        generate(0)
        return res
            
