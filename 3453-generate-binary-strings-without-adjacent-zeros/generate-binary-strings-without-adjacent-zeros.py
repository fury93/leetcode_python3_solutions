class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []
        def generate(digits, i):
            if i == 0:
                res.append(''.join(digits))
                return

            if not digits or digits[-1] != '0':
                digits.append('0')
                generate(digits, i-1)
                digits.pop()

            digits.append('1')
            generate(digits, i-1)
            digits.pop()
            
        generate([], n)
        return res
            
