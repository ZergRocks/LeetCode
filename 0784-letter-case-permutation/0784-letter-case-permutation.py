class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = set()
        n = len(s)

        for i in range(2 ** n):
            new_str = ''
            for j in range(n):
                if i & (1 << j):
                    new_str += s[j].upper()
                else:
                    new_str += s[j].lower()
            result.add(new_str)

        return result
                
                